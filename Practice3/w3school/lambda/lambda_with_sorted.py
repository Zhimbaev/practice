
#ex1 сортировка по второму элементу
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  #

#ex2 сортировка по длине
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words) 

#ex3 сортировка по убыванию
numbers = [5, 2, 9, 1, 7]
sorted_desc = sorted(numbers, key=lambda x: -x)
print(sorted_desc) 

#ex4 сортивровка по модулю
numbers = [-5, 3, -2, 8]
sorted_abs = sorted(numbers, key=lambda x: abs(x))
print(sorted_abs) 

#ex5 сортровка неизменяемых листов по их сумме
tuples = [(1, 2), (3, 1), (2, 2)]
sorted_sum = sorted(tuples, key=lambda x: x[0] + x[1])
print(sorted_sum)