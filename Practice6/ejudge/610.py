a = int(input())
b = map(int, input().split())

y = map(lambda x: x != 0, b)
print(sum(y))