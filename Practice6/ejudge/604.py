a = int(input())

b = map(int, input().split())
c = map(int, input().split())

z = zip(b,c)

print(sum(x*y for x, y in z))
