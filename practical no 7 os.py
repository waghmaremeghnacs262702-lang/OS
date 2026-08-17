import threading
import time
import random


BUFFER_SIZE = 5


buffer = [None] * BUFFER_SIZE


in_index = 0
out_index = 0


empty = threading.Semaphore(BUFFER_SIZE)  
full = threading.Semaphore(0)            


mutex = threading.Lock()

def producer():
    global in_index

    for i in range(10):
        item = random.randint(1, 100)

        empty.acquire()

        with mutex:
            buffer[in_index] = item
            print(f"Producer produced: {item} at position {in_index}")

            in_index = (in_index + 1) % BUFFER_SIZE

        full.release()

        time.sleep(random.uniform(0.5, 1))


def consumer():
    global out_index

    for i in range(10):

        full.acquire()

        with mutex:
            item = buffer[out_index]
            buffer[out_index] = None

            print(f"Consumer consumed: {item} from position {out_index}")

            out_index = (out_index + 1) % BUFFER_SIZE

        empty.release()

        time.sleep(random.uniform(0.5, 1))


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()


producer_thread.join()
consumer_thread.join()

print("\nProducer-Consumer execution completed.")
