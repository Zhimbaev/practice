a = int(input())
b = input().split()
c = input().split()
d = input()

res = dict(zip(b, c))

print(res[d] if d in res else "Not found")