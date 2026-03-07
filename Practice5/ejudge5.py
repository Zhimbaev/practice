# 1


# import re

# s = input()

# x = re.match(r"Hello",s)

# print("Yes" if x else "No")


# 2

# import re

# a = input()
# b = input()

# x = re.search(b, a)

# print("Yes" if x else "No")


# 3


# import re

# a = input()
# b = input()

# x = re.findall(b,a)
# print(len(x))


# 4


# import re

# a = input()
# x = re.findall(r"\d",a)
# y = " ".join(x)
# print(y)


# 5


# import re

# a = input()  
# x = re.match(r'^[A-Za-z].*[0-9]$', a)
# print('Yes' if x else 'No')


# 6


# import re

# text = input()

# x = re.search(r'\S+@\S+\.\S+', text)

# if x:
#     print(x.group())
# else:
#     print("No email")


# 7


# import re

# text = input()      
# y = input()     
# x = input() 

# result = re.sub(y, x, text)

# print(result)



# 8


# import re

# text = input()      
# x = input()   

# parts = re.split(x, text)  
# print(','.join(parts))           



# 9


# import re

# text = input()

# words = re.findall(r'\b\w{3}\b', text)

# print(len(words))


# 10


# import re

# text = input()

# if re.search('cat|dog', text):
#     print("Yes")
# else:
#     print("No")


# 11


# import re

# text = input()

# up = re.findall(r'[A-Z]', text)

# print(len(up))


# 12


# import re

# text = input()

# seq = re.findall(r'\d{2,}', text)

# print(' '.join(seq))


# 13


# import re

# text = input()

# words = re.findall('\w+', text)

# print(len(words))


# 14


# import re

# text = input()

# pattern = re.compile(r'^\d+$') 

# print("Match" if pattern.match(text) else "No match")



# 15


# import re

# text = input()


# def double_digit(match):
#     return match.group() * 2


# result = re.sub(r'\d', double_digit, text)

# print(result)


# 16


# import re

# text = input()
# match = re.search(r'Name: (.+), Age: (.+)', text)

# if match:
#     name, age = match.groups()
#     print(name, age)


# 17


# import re

# text = input()

# dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)

# print(len(dates))


# 18


# import re

# S = input()
# P = input()

# pattern = re.escape(P)
# matches = re.findall(pattern, S)

# print(len(matches))


# 19


# import re

# text = input()

# pattern = re.compile(r'\b\w+\b')

# words = pattern.findall(text)

# print(len(words))