# ex1
# наследование без изменений
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)




class Student(Person):
    pass  #наследует от родителя все без изменений

x = Student("Mike", "Olsen")
x.printname()  #Mike Olsen


# ex2
class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)  # зоввет родительский 

y = Student("Anna", "Smith")
y.printname()  #Anna Smith


# ex3
class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationyear = year  # добавляет классу новое свойство и наследует от родительского

s1 = Student("Emily", "Clark", 2024)
print(s1.firstname, s1.lastname, s1.graduationyear)
#Emily Clark 2024


# ex4
class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationyear = year

    def welcome(self):
        print(
            f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}"
        ) #добавляет новый метод

s2 = Student("John", "Doe", 2023)
s2.welcome()  #Welcome John Doe to the class of 2023