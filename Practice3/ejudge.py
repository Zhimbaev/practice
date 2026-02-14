# # # # # a = int(input())
# # # # # x = 0
# # # # # c = 0

# # # # # while a > 0:
# # # # #     x = a % 10
# # # # #     if x % 2 == 0:
# # # # #         a //= 10
# # # # #         c = 1
# # # # #         continue
# # # # #     else:
# # # # #         c = 0
# # # # #         print("Not valid")
# # # # #         break
# # # # # if c == 1:
# # # # #     print("Valid")




# # # # # def isUsual(num):
# # # # #     if num <= 0:
# # # # #         return False

# # # # #     while num % 2 == 0:
# # # # #         num //= 2

# # # # #     while num % 3 == 0:
# # # # #         num //= 3

# # # # #     while num % 5 == 0:
# # # # #         num //= 5

# # # # #     return num == 1


# # # # # n = int(input())

# # # # # if isUsual(n):
# # # # #     print("Yes")
# # # # # else:
# # # # #     print("No")




# # # # words = {
# # # #     "ZER": "0",
# # # #     "ONE": "1",
# # # #     "TWO": "2",
# # # #     "THR": "3",
# # # #     "FOU": "4",
# # # #     "FIV": "5",
# # # #     "SIX": "6",
# # # #     "SEV": "7",
# # # #     "EIG": "8",
# # # #     "NIN": "9"
# # # # }

# # # # digits = {
# # # #     "0": "ZER",
# # # #     "1": "ONE",
# # # #     "2": "TWO",
# # # #     "3": "THR",
# # # #     "4": "FOU",
# # # #     "5": "FIV",
# # # #     "6": "SIX",
# # # #     "7": "SEV",
# # # #     "8": "EIG",
# # # #     "9": "NIN"
# # # # }

# # # # s = input()

# # # # num1 = ""
# # # # num2 = ""
# # # # operator = ""

# # # # i = 0
# # # # first_number = True

# # # # while i < len(s):

# # # #     if s[i] == "+" or s[i] == "-" or s[i] == "*":
# # # #         operator = s[i]
# # # #         first_number = False
# # # #         i += 1
# # # #         continue

# # # #     part = s[i:i+3]

# # # #     if first_number:
# # # #         num1 += words[part]
# # # #     else:
# # # #         num2 += words[part]

# # # #     i += 3


# # # # a = int(num1)
# # # # b = int(num2)

# # # # if operator == "+":
# # # #     result = a + b
# # # # elif operator == "-":
# # # #     result = a - b
# # # # else:
# # # #     result = a * b

# # # # result_str = str(result)
# # # # answer = ""

# # # # j = 0
# # # # while j < len(result_str):
# # # #     answer += digits[result_str[j]]
# # # #     j += 1

# # # # print(answer)


# # # class StringHandler:
# # #     def __init__(self):
# # #         self.s = ""

# # #     def getString(self):
# # #         self.s = input()

# # #     def printString(self):
# # #         print(self.s.upper())


# # # obj = StringHandler()
# # # obj.getString()
# # # obj.printString()



# # class Shape:
# #     def area(self):
# #         return 0

# # class Square(Shape):
# #     def __init__(self, length):
# #         self.length = length

# #     def area(self):
# #         result = self.length * self.length
# #         return result

# # n = int(input())
# # sq = Square(n)
# # print(sq.area())





# from math import sqrt
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"({self.x}, {self.y})")
#     def move(self, new_x,new_y):
#         self.x = new_x
#         self.y = new_y
    
#     def length(self, ot_point):
#         dx = self.x - ot_point.x
#         dy =  self.y - ot_point.y
#         return sqrt(dx**2+dy**2)

# x1,y1 = map(int,input().split())
# p1 = Point(x1,y1)
# p1.show()
# x2,y2 = map(int,input().split())
# p1.move(x2,y2)
# p1.show()
# x3,y3 = map(int,input().split())
# p2 = Point(x3,y3)
# distance = p1.length(p2)
# print(f"{distance:.2f}")




# class Account:
#     def __init__(self,owner, balance):
#         self.balance = balance
#         self.owner = owner
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "Insufficient Funds"
#         self.balance -=amount
#         return self.balance

# a,b = map(int, input().split())
# account = Account("User", a)
# print(account.withdraw(b))




# class Circle:
#     pi = 3.14159

#     def __init__(self,r):
#         self.r = r

#     def area(self):
#         return (self.r**2)*Circle.pi

# a = int(input())
# cir = Circle(a)
# areas = cir.area()
# print(f"{areas:.2f}")



# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def __init__(self, name, gpa):
#         super().__init__(name)
#         self.gpa = gpa
#     def display(self):
#         print(f"Student: {self.name}, GPA: {self.gpa}")

# a, b = map(str, input().split())
# student = Student(a,float(b))
# student.display()



# class Pair:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def add(self,new_a,new_b):
#         self.a +=new_a
#         self.b += new_b
#         return self.a, self.b
    
        

# a,b,c,d = map(int,input().split())
# pair_f = Pair(a,b)
# sum_num = pair_f.add(c,d)
# print(f"Result: {sum_num[0]} {sum_num[1]}")




# class Employee:
#     def __init__(self,name,base_salary):
#         self.name = name
#         self.base_salary = base_salary

#     def total_salary(self):
#         return self.base_salary
#     def get_name(self):
#         return self.name

# class Manager(Employee):
#     def __init__(self,name,base_salary, bonus_percent):
#         super().__init__(name, base_salary)
#         self.bonus_percent = bonus_percent
#     def total_salary(self):
#         return self.base_salary * (1 + self.bonus_percent / 100)

# class Developer(Employee):
#     def __init__(self,name,base_salary, completed_projects):
#         super().__init__(name, base_salary)
#         self.completed_projects = completed_projects
#     def total_salary(self):
#         return self.base_salary + self.completed_projects * 500

# class Intern(Employee):
#     def __init__(self,name, base_salary):
#         super().__init__(name,base_salary)


# data = input().split()
# position = data[0]
# name = data[1]
# base_salary = int(data[2])

# match position:
#     case "Manager":
#         bonus = int(data[3])
#         p = Manager(name, base_salary, bonus)
#     case "Developer":
#         projects = int(data[3])
#         p = Developer(name, base_salary, projects)
#     case "Intern":
#         p = Intern(name, base_salary)

# print(f"Name: {p.name}, Total: {p.total_salary():.2f}")




# numbers = list(map(int, input().split()))


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True



# primes = list(filter(lambda x: is_prime(x), numbers))

# if primes:
#     print(*primes)
# else:
#     print("No primes")





# n = int(input())
# arr = list(map(int, input().split()))
# q = int(input())

# for _ in range(q):
#     op = input().split()

#     if op[0] == "add":
#         x = int(op[1])
#         arr = list(map(lambda a: a + x, arr))

#     elif op[0] == "multiply":
#         x = int(op[1])
#         arr = list(map(lambda a: a * x, arr))

#     elif op[0] == "power":
#         x = int(op[1])
#         arr = list(map(lambda a: a ** x, arr))

#     elif op[0] == "abs":
#         arr = list(map(lambda a: abs(a), arr))

# print(*arr)