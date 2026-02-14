# ex1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)
print(p1.name)  # Emil
print(p1.age)   # 36


# ex2
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)
print(p1.name, p1.age)  # Output: Emil 18
print(p2.name, p2.age)  # Output: Tobias 25


# ex3
class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")
print(p1.name)    # Linus
print(p1.age)     # 30
print(p1.city)    # Oslo
print(p1.country) # Norway


# ex4
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()  # вызов другого метода
        print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()  # Hello, Tobias! Welcome to our website.