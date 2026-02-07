#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#ex3
for x in "Hello World":
    if x == " ":
        break
    print("Char:", x)

#ex4
colors = ["red", "green", "blue"]
for c in colors:
    if c == "green":
        break
    print("Color:", c)

#ex5
for i in range(5, 15):
    if i == 7:
        break
    print("Counter", i)