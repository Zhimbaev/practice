a = int(input())
b = map(int,input().split())

sq_sum = sum(map(lambda x: x**2, b))
print(sq_sum)