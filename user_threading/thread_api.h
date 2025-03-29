
#ifndef UTHREADS_API_H
#define UTHREADS_API_H

#include <stddef.h>

#define MAX_THREADS 10
#define STACK_SIZE 4096

typedef void (*thread_start_func)(void);

/**
 * Initialize the threading system with a given quantum size in microseconds.
 * This must be called before using any other functions.
 *
 * @param quantum_usecs The size of each time slice (quantum).
 * @return 0 if success, -1 on failure.
 */
int thread_system_init(int quantum_usecs);

/**
 * Creates a new thread starting at the given entry point.
 *
 * @param func The function the new thread will run.
 * @return The thread ID (0–9) or -1 on error.
 */
int thread_create(thread_start_func func);

/**
 * Terminates a thread.
 * If the main thread (ID 0) exits, the program terminates.
 *
 * @param tid Thread ID to terminate.
 * @return 0 if success, -1 on error.
 */
int thread_exit(int tid);

/**
 * Blocks a thread (except main).
 *
 * @param tid Thread ID to block.
 * @return 0 if success, -1 on error.
 */
int thread_block(int tid);

/**
 * Unblocks a previously blocked thread.
 *
 * @param tid Thread ID to unblock.
 * @return 0 if success, -1 on error.
 */
int thread_unblock(int tid);

/**
 * Sleeps the calling thread for a number of quantums.
 *
 * @param num_quantums Number of quantum cycles to sleep.
 * @return 0 if success, -1 on error.
 */
int thread_sleep(int num_quantums);

#endif // UTHREADS_API_H
