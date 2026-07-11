from multiprocessing import Process, Semaphore, Lock, Array, Value
import time
import random

# Total buffer size (how many items the buffer can hold at once)
BUFFER_SIZE = 5

# Total number of items to produce and consume
ITEM_COUNT = 10


# Producer Function
def producer(buffer, in_index, out_index, empty, full, mutex):
    for _ in range(ITEM_COUNT):
        # Produce a random number
        item = random.randint(1, 100)

        # Wait until there is at least one empty slot
        empty.acquire()

        # Enter critical section
        mutex.acquire()

        # Place the item in the buffer
        idx = in_index.value
        buffer[idx] = item
        print(f"[Producer] Produced item {item} at index {idx}", flush=True)

        # Update in_index circularly
        in_index.value = (idx + 1) % BUFFER_SIZE

        # Leave critical section
        mutex.release()

        # Signal that one item is available
        full.release()

        # Simulate delay
        time.sleep(random.uniform(0.1, 0.3))


# Consumer Function
def consumer(buffer, in_index, out_index, empty, full, mutex):
    print("[Consumer] Process started", flush=True)

    for _ in range(ITEM_COUNT):
        # Wait until at least one item is available
        full.acquire()

        # Enter critical section
        mutex.acquire()

        # Remove item from buffer
        idx = out_index.value
        item = buffer[idx]
        print(f"[Consumer] Consumed item {item} from index {idx}", flush=True)

        # Update out_index circularly
        out_index.value = (idx + 1) % BUFFER_SIZE

        # Leave critical section
        mutex.release()

        # Signal that one slot is free
        empty.release()

        # Simulate delay
        time.sleep(random.uniform(0.1, 0.3))


def main():
    # Create shared memory
    buffer = Array('i', BUFFER_SIZE)
    in_index = Value('i', 0)
    out_index = Value('i', 0)

    # Synchronization primitives
    empty = Semaphore(BUFFER_SIZE)  # Buffer initially empty
    full = Semaphore(0)             # No items initially
    mutex = Lock()                  # Mutual exclusion lock
    print("Meghna waghmare")
    print("Starting processes...", flush=True)

    # Create producer and consumer processes
    p = Process(
        target=producer,
        args=(buffer, in_index, out_index, empty, full, mutex)
    )

    c = Process(
        target=consumer,
        args=(buffer, in_index, out_index, empty, full, mutex)
    )

    # Start processes
    p.start()
    c.start()

    # Wait for both to finish
    p.join()
    c.join()

    print("Producer and Consumer processes have finished.", flush=True)


# Run only when executed directly
if __name__ == "__main__":
    main()
