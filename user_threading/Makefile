
CC = gcc
CFLAGS = -Wall -g

OBJS = thread_manager.o main.o

all: main

main: $(OBJS)
	$(CC) $(CFLAGS) -o main $(OBJS)

thread_manager.o: thread_manager.c thread_api.h
	$(CC) $(CFLAGS) -c thread_manager.c

main.o: main.c thread_api.h
	$(CC) $(CFLAGS) -c main.c

clean:
	rm -f *.o main
