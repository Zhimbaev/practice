#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#ex2

for char in "banana":
    if char == "a":
        continue
    print("Not 'a':", char)

#ex3
for i in range(5):
    if i % 2 == 0:
        continue
    print("Odd num:", i)

#ex4
nums = [1, 0, 3]
for n in nums:
    if n == 0:
        continue
    print("Num:", n)

#ex5
for i in range(10, 50, 10):
    if i < 30:
        continue
    print("Large values:", i)