# Generator that generates squares up to N
def squares_up_to_n(N):
    for i in range(N + 1):
        yield i ** 2

print("Squares up to 5:")
for val in squares_up_to_n(5):
    print(val, end=" ")
print("\n")


# Generator to print even numbers between 0 and n (input from console)
n = int(input("Enter n for even numbers: "))

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

print("Even numbers from 0 to", n, ":", end=" ")
print(", ".join(str(x) for x in even_numbers(n)))
print()


# Function with a generator for numbers divisible by 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("Numbers divisible by 3 and 4 up to 50:")
for val in divisible_by_3_and_4(50):
    print(val, end=" ")
print("\n")


# Generator called squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

print("Squares from 3 to 7:")
for val in squares(3, 7):
    print(val, end=" ")
print("\n")


# Generator that returns all numbers from n down to 0
def countdown(n):
    for i in range(n, -1, -1):
        yield i

print("Countdown from 10:")
for val in countdown(10):
    print(val, end=" ")
print()