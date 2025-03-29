#include "thread_api.h"
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/time.h>
#include <setjmp.h>
#include <string.h>

// ARCHITECTURE HELPERS 
// Architecture-specific constants for jmp_buf indices (SP and PC)
#ifdef __x86_64__
#define JB_SP 6
#define JB_PC 7
#elif __i386__
#define JB_SP 4
#define JB_PC 5
#else
#error "Unsupported architecture"
#endif

// Translate virtual address (used from reference code)
typedef unsigned long address_t;
address_t translate_address(address_t addr) {
    address_t ret;
    asm volatile("xor %%fs:0x30,%0\n"
                 "rol $0x11,%0\n"
                 : "=g" (ret)
                 : "0" (addr));
    return ret;
}

// THREAD STRUCTURE 

typedef enum {READY, RUNNING, BLOCKED, SLEEPING, TERMINATED} thread_state;

typedef struct thread_t {
    int tid;                        // Thread ID
    thread_state state;            // Current state
    int sleep_quantums;            // Remaining quantums to sleep
    char stack[UTHREAD_STACK_BYTES]; // Stack memory for this thread
    sigjmp_buf env;                // Saved context
} thread_t;

//  GLOBALS

static thread_t threads[UTHREAD_MAX_THREADS]; // Thread array
int current_tid = 0;                          // Currently running thread ID
static int quantum_usecs = 0;                // Quantum length in microseconds

// SCHEDULER

int find_next_ready_thread();

void scheduler_handler(int sig) {
    // Timer interrupt occurred, perform context switch
    printf("[Scheduler] Quantum expired. Switching threads...\n");

    // Handle sleeping threads
    for (int i = 0; i < UTHREAD_MAX_THREADS; ++i) {
        if (threads[i].state == SLEEPING) {
            threads[i].sleep_quantums--;
            printf("[Scheduler] Thread %d sleeping... remaining: %d\n", i, threads[i].sleep_quantums);
            if (threads[i].sleep_quantums <= 0) {
                threads[i].state = READY;
                printf("[Scheduler] Thread %d woke up and is now READY\n", i);
            }
        }
    }

    // Save context of current thread
    if (sigsetjmp(threads[current_tid].env, 1) != 0) {
        return; // Will return here when context is restored
    }

    if (threads[current_tid].state == RUNNING) {
        threads[current_tid].state = READY;
        printf("[Scheduler] Thread %d set to READY\n", current_tid);
    }

    // Select next READY thread
    int next_tid = find_next_ready_thread();
    if (next_tid == -1) {
        threads[current_tid].state = RUNNING; // Continue with current
        printf("[Scheduler] No READY thread found. Staying on thread %d\n", current_tid);
        return;
    }

    printf("[Scheduler] Switching from thread %d to thread %d\n", current_tid, next_tid);
    current_tid = next_tid;
    threads[current_tid].state = RUNNING;
    siglongjmp(threads[current_tid].env, 1);
}

// INITIALIZATION

int uthread_system_init(int quantum) {
    if (quantum <= 0 || quantum > 1000000) {
        return -1;
    }
    quantum_usecs = quantum;

    // Set all threads to terminated initially
    for (int i = 0; i < UTHREAD_MAX_THREADS; ++i) {
        threads[i].state = TERMINATED;
    }

    // Setup main thread
    threads[0].tid = 0;
    threads[0].state = RUNNING;
    threads[0].sleep_quantums = 0;

    if (sigsetjmp(threads[0].env, 1) != 0) {
        return 0;
    }

    // Configure timer
    struct sigaction sa;
    memset(&sa, 0, sizeof(sa));
    sa.sa_handler = scheduler_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    if (sigaction(SIGVTALRM, &sa, NULL) < 0) {
        perror("sigaction failed");
        return -1;
    }

    struct itimerval timer;
    timer.it_value.tv_sec = 0;
    timer.it_value.tv_usec = quantum_usecs;
    timer.it_interval.tv_sec = 0;
    timer.it_interval.tv_usec = quantum_usecs;

    printf("[Debug] Setting virtual timer using setitimer()\n");

    if (setitimer(ITIMER_VIRTUAL, &timer, NULL) < 0) {
        perror("setitimer failed");
        return -1;
    }

    printf("[Init] Timer set with quantum = %d usec\n", quantum_usecs);
    return 0;
}

//  THREAD MANAGEMENT

int uthread_create(uthread_entry entry_func) {
    int tid = -1;
    for (int i = 1; i < UTHREAD_MAX_THREADS; ++i) {
        if (threads[i].state == TERMINATED) {
            tid = i;
            break;
        }
    }
    if (tid == -1) return -1;

    threads[tid].tid = tid;
    threads[tid].state = READY;
    threads[tid].sleep_quantums = 0;

    if (sigsetjmp(threads[tid].env, 1) == 0) {
        address_t sp = (address_t)(threads[tid].stack + UTHREAD_STACK_BYTES - sizeof(address_t));
        address_t pc = (address_t)entry_func;

        threads[tid].env->__jmpbuf[JB_SP] = translate_address(sp);
        threads[tid].env->__jmpbuf[JB_PC] = translate_address(pc);
        sigemptyset(&threads[tid].env->__saved_mask);
        return tid;
    }
    return 0;
}

int find_next_ready_thread() {
    int next = (current_tid + 1) % UTHREAD_MAX_THREADS;
    for (int i = 0; i < UTHREAD_MAX_THREADS - 1; ++i) {
        if (threads[next].state == READY) {
            return next;
        }
        next = (next + 1) % UTHREAD_MAX_THREADS;
    }
    return -1;
}

int uthread_block(int tid) {
    if (tid <= 0 || tid >= UTHREAD_MAX_THREADS) return -1;
    if (threads[tid].state != READY && threads[tid].state != RUNNING) return -1;
    threads[tid].state = BLOCKED;
    if (tid == current_tid) scheduler_handler(0);
    return 0;
}

int uthread_unblock(int tid) {
    if (tid < 0 || tid >= UTHREAD_MAX_THREADS) return -1;
    if (threads[tid].state == BLOCKED) {
        threads[tid].state = READY;
        return 0;
    }
    return -1;
}

int uthread_exit(int tid) {
    if (tid < 0 || tid >= UTHREAD_MAX_THREADS) return -1;
    if (threads[tid].state == TERMINATED) return -1;
    if (tid == 0) {
        printf("[uthread_exit] Main thread exiting. Terminating process.\n");
        exit(0);
    }
    threads[tid].state = TERMINATED;
    if (tid == current_tid) scheduler_handler(0);
    return 0;
}

int uthread_sleep_quantums(int num_quantums) {
    if (current_tid == 0 || num_quantums <= 0) return -1;
    threads[current_tid].state = SLEEPING;
    threads[current_tid].sleep_quantums = num_quantums;
    scheduler_handler(0);
    return 0;
}
