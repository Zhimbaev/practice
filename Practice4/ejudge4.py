# 1

def fun(m):
    for x in range(1, m+1):
        yield x ** 2

n = int(input())

for i in fun(n):
    print(i)