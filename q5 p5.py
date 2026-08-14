import threading
import math


def calculate_factorial(n):
    result = math.factorial(n)
    print(f"Thread {threading.current_thread().name}: Factorial of {n} = {result}")


thread1 = threading.Thread(target=calculate_factorial, args=(5,), name="Thread-1")
thread2 = threading.Thread(target=calculate_factorial, args=(6,), name="Thread-2")
thread3 = threading.Thread(target=calculate_factorial, args=(7,), name="Thread-3")


thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("All threads completed.")
