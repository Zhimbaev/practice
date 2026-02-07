#ex1
i = 1
while i < 10:
    if i == 3:
        break
    print("Num:", i)
    i += 1

#ex2
while True:
    print("Looping...")
    break 

#ex3
box = 1
while box < 5:
    print("Checking box", box)
    if box == 2:
        print("Found it")
        break
    box += 1

#ex4
i = 0
while i < 100:
    print("Searching......")
    if i == 1:
        break
    i += 1

#ex5
temp = 20
while temp < 30:
    print("Temp:", temp)
    if temp == 22:
        print("Alert")
        break
    temp += 1