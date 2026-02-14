# ex1
class Person:
    #Parent class
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(self.first_name, self.last_name)


class SimpleStudent(Person):
    # Child class свойства переходят с род
    pass


person = Person("John", "Doe")
person.print_name()  # John Doe

simple_student = SimpleStudent("Mike", "Olsen")
simple_student.print_name()  # Mike Olsen


# ex2
# использование super()
class Student(Person):
    # Добавление graduation к child class
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name) # берет значения из родительского но с добавлением своих
        self.graduation_year = graduation_year 

    def welcome(self):
        print(f"Welcome", self.first_name, self.last_name, "to the class of", self.graduation_year)


student = Student("Anna", "Smith", 2026)
student.print_name()  # Anna Smith
student.welcome()     # Welcome Anna Smith to the class of 2026


# ex3
class LoudStudent(Person):
    def print_name(self): # берет свойства принятия от род
        print(self.first_name.upper(), self.last_name.upper()) 


loud_student = LoudStudent("Emma", "Brown")
loud_student.print_name()  #EMMA BROWN


# ex4

class Independent: # не принимает никакие значения, просто функция
    def greet(self):
        print("I am independent!")


ind = Independent()
ind.greet() #I am independent!