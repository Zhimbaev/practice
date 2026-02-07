#ex1
i = 0
while i < 3:
    i += 1
    if i == 2:
        continue
    print("Num", i)

#ex2
i = 0
while i < 4:
    i += 1
    if i % 2 != 0:
        continue
    print("Even num", i)


#ex3
i = -2
while i < 2:
    i += 1
    if i < 0:
        continue
    print("Positive", i)

#ex4
status = 0
while status < 3:
    status += 1
    if status == 2:
        print("Skip error.....")
        continue
    print("Status ", status)

#ex5
i = 0
word = "cat"
while i < len(word):
    char = word[i]
    i += 1
    if char == "a":
        continue
    print("char", char)