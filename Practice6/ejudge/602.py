n = int(input())
b = map(int, input().split())

even_num = list(filter(lambda x: x%2==0, b))
print(len(even_num))