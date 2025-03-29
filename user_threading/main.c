#include "thread_api.h"
#include <stdio.h>

int tid1, tid2, tid3, tid4, tid5;

void thread_a() {
    while (1) {
        printf("[Thread A] Running...\n");
    }
}

void thread_b() {
    int count = 0;
    while (1) {
        printf("[Thread B] Sleeping for 3 quantums...\n");
        uthread_sleep_quantums(3);
        printf("[Thread B] Woke up! Count = %d\n", ++count);
    }
}

void thread_c() {
    printf("[Thread C] Blocking Thread A\n");
    uthread_block(tid1);
    printf("[Thread C] Sleeping 5 quantums before unblocking Thread A\n");
    uthread_sleep_quantums(5);
    printf("[Thread C] Unblocking Thread A\n");
    uthread_unblock(tid1);
    printf("[Thread C] Exiting\n");
    uthread_exit(tid3);
}

void thread_d() {
    for (int i = 0; i < 3; i++) {
        printf("[Thread D] Loop %d\n", i);
        uthread_sleep_quantums(2);
    }
    printf("[Thread D] Exiting\n");
    uthread_exit(tid4);
}

void thread_e() {
    int counter = 0;
    while (1) {
        printf("[Thread E] Running... (%d)\n", ++counter);
    }
}

int main() {
    printf("[Main] Initializing uthreads system...\n");
    if (uthread_system_init(100000) != 0) {
        printf("Failed to initialize uthreads.\n");
        return 1;
    }

    tid1 = uthread_create(thread_a);
    tid2 = uthread_create(thread_b);
    tid3 = uthread_create(thread_c);
    tid4 = uthread_create(thread_d);
    tid5 = uthread_create(thread_e);

    printf("[Main] Created threads: A=%d, B=%d, C=%d, D=%d, E=%d\n", tid1, tid2, tid3, tid4, tid5);

    for (int i = 1; i <= 10; ++i) {
        printf("[Main] Loop %d\n", i);
    }

    printf("[Main] Exiting main thread.\n");
    uthread_exit(0);
    return 0;
}
