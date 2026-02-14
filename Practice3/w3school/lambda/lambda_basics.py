# ex1
add_ten = lambda a: a + 10
print(add_ten(5))

# ex2
multiply = lambda a, b: a * b
print(multiply(5, 6))

# ex3
sum_three = lambda a, b, c: a + b + c
print(sum_three(5, 6, 2))

# ex4
def make_multiplier(n):
    return lambda a: a * n

# ex5
def make_multiplier(n):
    return lambda a: a * n

double = make_multiplier(2)
print(double(11))