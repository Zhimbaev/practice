import re

def Ex1():
    txt = input("Enter string for Ex1: ")
    matches = re.findall(r"ab*", txt)
    print("Matches:", matches)

def Ex2():
    txt = input("Enter string for Ex2: ")
    matches = re.findall(r"ab{2,3}", txt)
    print("Matches:", matches)

def Ex3():
    txt = input("Enter string for Ex3: ")
    matches = re.findall(r"[a-z]+_[a-z]+", txt)
    print("Matches:", matches)

def Ex4():
    txt = input("Enter string for Ex4: ")
    matches = re.findall(r"[A-Z][a-z]+", txt)
    print("Matches:", matches)

def Ex5():
    txt = input("Enter string for Ex5: ")
    matches = re.findall(r"a.*?b", txt)
    print("Matches:", matches)

def Ex6():
    txt = input("Enter string for Ex6: ")
    new_txt = re.sub(r"[ ,\.]", ":", txt)
    print("Result:", new_txt)

def Ex7():
    txt = input("Enter snake_case string for Ex7: ")
    components = txt.split("_")
    camel_case = components[0] + "".join(x.title() for x in components[1:])
    print("CamelCase:", camel_case)

def Ex8():
    txt = input("Enter CamelCase string for Ex8: ")
    parts = re.findall(r"[A-Z][a-z]*", txt)
    print("Split words:", parts)

def Ex9():
    txt = input("Enter string for Ex9: ")
    new_txt = re.sub(r"([A-Z])", r" \1", txt).strip()
    print("Result:", new_txt)

def Ex10():
    txt = input("Enter CamelCase string for Ex10: ")
    snake_case = re.sub(r"([A-Z])", r"_\1", txt).lower()
    print("snake_case:", snake_case)

def Gen_Ex(x):
    match x:
        case 1: Ex1()
        case 2: Ex2()
        case 3: Ex3()
        case 4: Ex4()
        case 5: Ex5()
        case 6: Ex6()
        case 7: Ex7()
        case 8: Ex8()
        case 9: Ex9()
        case 10: Ex10()

while True:
    a = input("\nPress any button to start or 'q' to quit: ")
    if a.lower() == 'q':
        break

    while True:
        try:
            b = int(input("Choose ex 1-10: "))
            print()
            if 1 <= b <= 10:
                Gen_Ex(b)
                break
            else:
                print("Enter number 1-10")
        except ValueError:
            print("Enter a NUMBER")