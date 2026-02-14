numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#ex1
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
#ex2
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
#ex3
greater_than_4 = list(filter(lambda x: x > 4, numbers))
print(greater_than_4) 
#ex4
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)  
#ex5
multiples_of_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(multiples_of_3)