import threading


def print_even():
    print("Even Numbers:")
    for i in range(1, 11):
        if i % 2 == 0:
            print(i)

def print_odd():
    print("Odd Numbers:")
    for i in range(1, 11):
        if i % 2 != 0:
            print(i)

def reverse_string():
    text = "Hello World"
    reversed_text = text[::-1]
    print("Original String:", text)
    print("Reversed String:", reversed_text)

t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)
t3 = threading.Thread(target=reverse_string)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All threads completed.")
