
numbers = [1, 2, 3, 4, 5]
#ex1
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  

#ex2
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  

#ex3
str_numbers = list(map(lambda x: str(x), numbers))
print(str_numbers)  

#ex4
added = list(map(lambda x: x + 5, numbers))
print(added) 

#ex5
negated = list(map(lambda x: -x, numbers))
print(negated)