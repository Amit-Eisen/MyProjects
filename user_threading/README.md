# user_threading

A simple user-level thread manager implemented in C, using `setitimer()` and `SIGVTALRM` for preemptive round-robin scheduling.

## ✨ Features

- Supports up to 10 concurrent threads.
- Preemptive round-robin scheduler.
- Thread states: `READY`, `RUNNING`, `BLOCKED`, `SLEEPING`, `TERMINATED`.
- Functions to block, unblock, terminate, and sleep threads.
- Implemented with low-level context switching using `sigsetjmp`/`siglongjmp`.

## 📁 Files

- `thread_manager.c` — Core implementation of the thread system.
- `thread_api.h` — Public API for thread operations.
- `main.c` — Demo/test for creating and managing threads.
- `Makefile` — Builds the project.
- `Dockerfile` — Runs the project inside a clean container.

## 🚀 Run Instructions (with Docker)

```bash
# Build the image
docker build -t user_threading .

# Run the container
docker run --rm user_threading
