a = int(input())
b = list(map(int,input().split()))
x = all(n >=0 for n in b)
print("Yes" if x else "No")