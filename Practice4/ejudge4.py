# # # # # # # # # # # 1

# # # # # # # # # # def fun(m):
# # # # # # # # # #     for x in range(1, m+1):
# # # # # # # # # #         yield x ** 2

# # # # # # # # # # n = int(input())

# # # # # # # # # # for i in fun(n):
# # # # # # # # # #     print(i)


# # # # # # # # # # 2

# # # # # # # # # def even_numbers(n):
# # # # # # # # #     i = 0
# # # # # # # # #     while i <= n:
# # # # # # # # #         if i % 2 == 0:
# # # # # # # # #             yield i
# # # # # # # # #         i += 1

# # # # # # # # # n = int(input())
# # # # # # # # # first = True
# # # # # # # # # for number in even_numbers(n):
# # # # # # # # #     if first:
# # # # # # # # #         print(number, end="")
# # # # # # # # #         first = False
# # # # # # # # #     else:
# # # # # # # # #         print("," + str(number), end="")


# # # # # # # # # 3


# # # # # # # # def divisible_by_3_and_4(n):
# # # # # # # #     i = 0
# # # # # # # #     while i <= n:
# # # # # # # #         if i % 3 == 0 and i % 4 == 0:
# # # # # # # #             yield i
# # # # # # # #         i += 1

# # # # # # # # n = int(input())
# # # # # # # # first = True
# # # # # # # # for number in divisible_by_3_and_4(n):
# # # # # # # #     if first:
# # # # # # # #         print(number, end="")
# # # # # # # #         first = False
# # # # # # # #     else:
# # # # # # # #         print(" " + str(number), end="")


# # # # # # # # 4


# # # # # # # # def squares(a, b):
# # # # # # # #     i = a
# # # # # # # #     while i <= b:
# # # # # # # #         yield i * i
# # # # # # # #         i += 1

# # # # # # # # a, b = map(int, input().split())

# # # # # # # # for number in squares(a, b):
# # # # # # # #     print(number)


# # # # # # # # 5



# # # # # # # def countdown(n):
# # # # # # #     i = n
# # # # # # #     while i >= 0:
# # # # # # #         yield i
# # # # # # #         i -= 1

# # # # # # # n = int(input())

# # # # # # # for number in countdown(n):
# # # # # # #     print(number)


# # # # # # # 6 


# # # # # # def fibonacci(n):
# # # # # #     a = 0
# # # # # #     b = 1
# # # # # #     count = 0
# # # # # #     while count < n:
# # # # # #         yield a
# # # # # #         c = a + b
# # # # # #         a = b
# # # # # #         b = c
# # # # # #         count += 1

# # # # # # n = int(input())
# # # # # # first = True
# # # # # # for number in fibonacci(n):
# # # # # #     if first:
# # # # # #         print(number, end="")
# # # # # #         first = False
# # # # # #     else:
# # # # # #         print("," + str(number), end="")



# # # # # # 7


# # # # # class Reverse:
# # # # #     def __init__(self, s):
# # # # #         self.s = s
# # # # #         self.index = len(s) - 1

# # # # #     def __iter__(self):
# # # # #         return self

# # # # #     def __next__(self):
# # # # #         if self.index < 0:
# # # # #             raise StopIteration
# # # # #         char = self.s[self.index]
# # # # #         self.index -= 1
# # # # #         return char

# # # # # s = input()
# # # # # rev = Reverse(s)
# # # # # for c in rev:
# # # # #     print(c, end="")



# # # # # 8


# # # # def primes_up_to(n):
# # # #     i = 2
# # # #     while i <= n:
# # # #         is_prime = True
# # # #         j = 2
# # # #         while j * j <= i:
# # # #             if i % j == 0:
# # # #                 is_prime = False
# # # #                 break
# # # #             j += 1
# # # #         if is_prime:
# # # #             yield i
# # # #         i += 1

# # # # n = int(input())
# # # # first = True
# # # # for number in primes_up_to(n):
# # # #     if first:
# # # #         print(number, end="")
# # # #         first = False
# # # #     else:
# # # #         print(" " + str(number), end="")



# # # # 9


# # # def powers_of_two(n):
# # #     i = 0
# # #     while i <= n:
# # #         yield 2 ** i
# # #         i += 1

# # # n = int(input())
# # # first = True
# # # for number in powers_of_two(n):
# # #     if first:
# # #         print(number, end="")
# # #         first = False
# # #     else:
# # #         print(" " + str(number), end="")


# # # 10


# # def limited_cycle(lst, k):
# #     count = 0
# #     while count < k:
# #         i = 0
# #         while i < len(lst):
# #             yield lst[i]
# #             i += 1
# #         count += 1

# # lst = input().split()
# # k = int(input())
# # first = True
# # for item in limited_cycle(lst, k):
# #     if first:
# #         print(item, end="")
# #         first = False
# #     else:
# #         print(" " + str(item), end="")



# # 11



# import json

# source = json.loads(input())
# patch = json.loads(input())

# def apply_patch(s, p):
#     for key in p:
#         if p[key] is None:
#             if key in s:
#                 del s[key]
#         elif isinstance(p[key], dict) and key in s and isinstance(s[key], dict):
#             apply_patch(s[key], p[key])
#         else:
#             s[key] = p[key]

# apply_patch(source, patch)

# print(json.dumps(source, sort_keys=True, separators=(',', ':')))