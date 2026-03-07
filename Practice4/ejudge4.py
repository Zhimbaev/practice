# # # # # # # # # # # # 1

# # # # # # # # # # # def fun(m):
# # # # # # # # # # #     for x in range(1, m+1):
# # # # # # # # # # #         yield x ** 2

# # # # # # # # # # # n = int(input())

# # # # # # # # # # # for i in fun(n):
# # # # # # # # # # #     print(i)


# # # # # # # # # # # 2

# # # # # # # # # # def even_numbers(n):
# # # # # # # # # #     i = 0
# # # # # # # # # #     while i <= n:
# # # # # # # # # #         if i % 2 == 0:
# # # # # # # # # #             yield i
# # # # # # # # # #         i += 1

# # # # # # # # # # n = int(input())
# # # # # # # # # # first = True
# # # # # # # # # # for number in even_numbers(n):
# # # # # # # # # #     if first:
# # # # # # # # # #         print(number, end="")
# # # # # # # # # #         first = False
# # # # # # # # # #     else:
# # # # # # # # # #         print("," + str(number), end="")


# # # # # # # # # # 3


# # # # # # # # # def divisible_by_3_and_4(n):
# # # # # # # # #     i = 0
# # # # # # # # #     while i <= n:
# # # # # # # # #         if i % 3 == 0 and i % 4 == 0:
# # # # # # # # #             yield i
# # # # # # # # #         i += 1

# # # # # # # # # n = int(input())
# # # # # # # # # first = True
# # # # # # # # # for number in divisible_by_3_and_4(n):
# # # # # # # # #     if first:
# # # # # # # # #         print(number, end="")
# # # # # # # # #         first = False
# # # # # # # # #     else:
# # # # # # # # #         print(" " + str(number), end="")


# # # # # # # # # 4


# # # # # # # # # def squares(a, b):
# # # # # # # # #     i = a
# # # # # # # # #     while i <= b:
# # # # # # # # #         yield i * i
# # # # # # # # #         i += 1

# # # # # # # # # a, b = map(int, input().split())

# # # # # # # # # for number in squares(a, b):
# # # # # # # # #     print(number)


# # # # # # # # # 5



# # # # # # # # def countdown(n):
# # # # # # # #     i = n
# # # # # # # #     while i >= 0:
# # # # # # # #         yield i
# # # # # # # #         i -= 1

# # # # # # # # n = int(input())

# # # # # # # # for number in countdown(n):
# # # # # # # #     print(number)


# # # # # # # # 6 


# # # # # # # def fibonacci(n):
# # # # # # #     a = 0
# # # # # # #     b = 1
# # # # # # #     count = 0
# # # # # # #     while count < n:
# # # # # # #         yield a
# # # # # # #         c = a + b
# # # # # # #         a = b
# # # # # # #         b = c
# # # # # # #         count += 1

# # # # # # # n = int(input())
# # # # # # # first = True
# # # # # # # for number in fibonacci(n):
# # # # # # #     if first:
# # # # # # #         print(number, end="")
# # # # # # #         first = False
# # # # # # #     else:
# # # # # # #         print("," + str(number), end="")



# # # # # # # 7


# # # # # # class Reverse:
# # # # # #     def __init__(self, s):
# # # # # #         self.s = s
# # # # # #         self.index = len(s) - 1

# # # # # #     def __iter__(self):
# # # # # #         return self

# # # # # #     def __next__(self):
# # # # # #         if self.index < 0:
# # # # # #             raise StopIteration
# # # # # #         char = self.s[self.index]
# # # # # #         self.index -= 1
# # # # # #         return char

# # # # # # s = input()
# # # # # # rev = Reverse(s)
# # # # # # for c in rev:
# # # # # #     print(c, end="")



# # # # # # 8


# # # # # def primes_up_to(n):
# # # # #     i = 2
# # # # #     while i <= n:
# # # # #         is_prime = True
# # # # #         j = 2
# # # # #         while j * j <= i:
# # # # #             if i % j == 0:
# # # # #                 is_prime = False
# # # # #                 break
# # # # #             j += 1
# # # # #         if is_prime:
# # # # #             yield i
# # # # #         i += 1

# # # # # n = int(input())
# # # # # first = True
# # # # # for number in primes_up_to(n):
# # # # #     if first:
# # # # #         print(number, end="")
# # # # #         first = False
# # # # #     else:
# # # # #         print(" " + str(number), end="")



# # # # # 9


# # # # def powers_of_two(n):
# # # #     i = 0
# # # #     while i <= n:
# # # #         yield 2 ** i
# # # #         i += 1

# # # # n = int(input())
# # # # first = True
# # # # for number in powers_of_two(n):
# # # #     if first:
# # # #         print(number, end="")
# # # #         first = False
# # # #     else:
# # # #         print(" " + str(number), end="")


# # # # 10


# # # def limited_cycle(lst, k):
# # #     count = 0
# # #     while count < k:
# # #         i = 0
# # #         while i < len(lst):
# # #             yield lst[i]
# # #             i += 1
# # #         count += 1

# # # lst = input().split()
# # # k = int(input())
# # # first = True
# # # for item in limited_cycle(lst, k):
# # #     if first:
# # #         print(item, end="")
# # #         first = False
# # #     else:
# # #         print(" " + str(item), end="")



# # # 11



# # import json

# # source = json.loads(input())
# # patch = json.loads(input())

# # def apply_patch(s, p):
# #     for key in p:
# #         if p[key] is None:
# #             if key in s:
# #                 del s[key]
# #         elif isinstance(p[key], dict) and key in s and isinstance(s[key], dict):
# #             apply_patch(s[key], p[key])
# #         else:
# #             s[key] = p[key]

# # apply_patch(source, patch)

# # print(json.dumps(source, sort_keys=True, separators=(',', ':')))



# 12


# import json
# import sys

# def diff(a, b, path=""):
#     differences = []

#     keys = set(a.keys()) | set(b.keys())
#     for key in sorted(keys):
#         a_val = a.get(key, "<missing>")
#         b_val = b.get(key, "<missing>")
#         current_path = f"{path}.{key}" if path else key

#         if isinstance(a_val, dict) and isinstance(b_val, dict):
#             differences.extend(diff(a_val, b_val, current_path))
#         elif a_val != b_val:
#             def serialize(val):
#                 if val == "<missing>":
#                     return "<missing>"
#                 return json.dumps(val, separators=(',',':'))

#             differences.append(f"{current_path} : {serialize(a_val)} -> {serialize(b_val)}")

#     return differences

# a = json.loads(sys.stdin.readline())
# b = json.loads(sys.stdin.readline())

# result = diff(a, b)
# if result:
#     print("\n".join(result))
# else:
#     print("No differences")



# 13


# import json

# def resolve(data, query):
#     current = data

#     for part in query.split('.'):
        
#         while '[' in part:
#             key, rest = part.split('[', 1)
#             if key:  
#                 if not isinstance(current, dict) or key not in current:
#                     return "NOT_FOUND"
#                 current = current[key]
#             idx, part = rest.split(']', 1)
#             idx = int(idx)
#             if not isinstance(current, list) or idx >= len(current):
#                 return "NOT_FOUND"
#             current = current[idx]
#         if part:  
#             if not isinstance(current, dict) or part not in current:
#                 return "NOT_FOUND"
#             current = current[part]
#     return json.dumps(current, separators=(',', ':'))

# data = json.loads(input())
# q = int(input())
# for _ in range(q):
#     query = input().strip()
#     print(resolve(data, query))

# 14 


# import datetime

# a = input()
# b = input()
# d_1 = datetime.datetime.strptime(a, "%Y-%m-%d UTC%z")
# d_2 = datetime.datetime.strptime(b, "%Y-%m-%d UTC%z")

# delta = d_1 - d_2
# print(abs(delta).days)


# 15 



# from datetime import datetime, timedelta

# a = input().strip()
# b = input().strip()

# b_day = datetime.strptime(a, "%Y-%m-%d UTC%z")
# c_day = datetime.strptime(b, "%Y-%m-%d UTC%z")

# year = c_day.year
# try:
#     next_bday = datetime(year, b_day.month, b_day.day, tzinfo=b_day.tzinfo)
# except ValueError:  
#     next_bday = datetime(year, 2, 28, tzinfo=b_day.tzinfo)

# if next_bday < c_day:
#     year += 1
#     try:
#         next_bday = datetime(year, b_day.month, b_day.day, tzinfo=b_day.tzinfo)
#     except ValueError:
#         next_bday = datetime(year, 2, 28, tzinfo=b_day.tzinfo)

# delta = next_bday - c_day
# days = delta.days + (delta.seconds > 0)
# print(days)


# 16


# import datetime

# a, b = input().strip(), input().strip()

# s_day = datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S UTC%z")
# e_day = datetime.datetime.strptime(b, "%Y-%m-%d %H:%M:%S UTC%z")

# delta = abs((s_day - e_day).total_seconds())
# print(int(delta))


# 17


# import math

# # Ввод данных
# R = float(input())
# x1, y1 = map(float, input().split())
# x2, y2 = map(float, input().split())

# dx = x2 - x1
# dy = y2 - y1

# length_AB = math.hypot(dx, dy)

# a = dx**2 + dy**2
# b = 2 * (dx*x1 + dy*y1)
# c = x1**2 + y1**2 - R**2

# discriminant = b**2 - 4*a*c

# if discriminant < 0:
#     print("0.0000000000")
# else:
#     sqrt_D = math.sqrt(discriminant)
#     t1 = (-b - sqrt_D) / (2*a)
#     t2 = (-b + sqrt_D) / (2*a)
    
#     t_start = max(0, min(t1, t2))
#     t_end = min(1, max(t1, t2))
    
#     if t_start > t_end:
#         print("0.0000000000")
#     else:
#         inside_length = (t_end - t_start) * length_AB
#         print(f"{inside_length:.10f}")


# 18 


# x1, y1 = map(float, input().split())
# x2, y2 = map(float, input().split())

# x_reflect = x1 + y1 * (x2 - x1) / (y1 + y2)
# y_reflect = 0.0

# print(f"{x_reflect:.10f} {y_reflect:.10f}")


# 19 


# import math

# def solve():
#     try:
#         line1 = input().split()
#         if not line1: return
#         r = float(line1[0])
        
#         line2 = input().split()
#         ax, ay = map(float, line2)
        
#         line3 = input().split()
#         bx, by = map(float, line3)
#     except EOFError:
#         return

#     # Euclidean distance between A and B
#     dist_ab = math.sqrt((ax - bx)**2 + (ay - by)**2)
    
#     # Distance from origin to A and B
#     da = math.sqrt(ax**2 + ay**2)
#     db = math.sqrt(bx**2 + by**2)
    
#     # Check if the segment AB intersects the circle
#     # We use the dot product to find the closest point on the segment AB to the origin
#     # Segment: P(t) = A + t(B-A), 0 <= t <= 1
#     dx, dy = bx - ax, by - ay
#     t = - (ax * dx + ay * dy) / (dx**2 + dy**2) if (dx**2 + dy**2) != 0 else 0
    
#     # Restrict t to the segment [0, 1]
#     t = max(0, min(1, t))
#     closest_x = ax + t * dx
#     closest_y = ay + t * dy
#     dist_to_origin = math.sqrt(closest_x**2 + closest_y**2)
    
#     if dist_to_origin >= r - 1e-9:
#         # Path is not blocked
#         print(f"{dist_ab:.10f}")
#     else:
#         # Path is blocked: Tangent A + Arc + Tangent B
#         # Length of tangents
#         l1 = math.sqrt(abs(da**2 - r**2))
#         l2 = math.sqrt(abs(db**2 - r**2))
        
#         # Angles
#         angle_a = math.atan2(ay, ax)
#         angle_b = math.atan2(by, bx)
        
#         # Total central angle
#         total_angle = abs(angle_a - angle_b)
#         if total_angle > math.pi:
#             total_angle = 2 * math.pi - total_angle
            
#         # Angles of the tangent parts
#         alpha1 = math.acos(r / da)
#         alpha2 = math.acos(r / db)
        
#         # Arc angle
#         arc_angle = total_angle - alpha1 - alpha2
#         arc_length = max(0, arc_angle) * r
        
#         print(f"{l1 + l2 + arc_length:.10f}")

# solve()


# 20



# n_commands = int(input())

# g, n = 0, 0

# for _ in range(n_commands):
#     line = input().split()
#     if not line: continue
    
#     scope = line[0]
#     value = int(line[1])
    
#     if scope == "global":
#         g += value
#     elif scope == "nonlocal":
#         n += value
# print(g, n)