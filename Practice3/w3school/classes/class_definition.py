
# ex1
class MyClass:
    x = 5  # атрибут класса


obj = MyClass()    # создаём объект
print("ex1:", obj.x)  # выводим значение атрибута   


# ex2
class Person:
    def __init__(self, name, age):
        self.name = name   
        self.age = age      

    def say_hello(self):
        return f"Привет, меня зовут {self.name}, мне {self.age} лет"


person1 = Person("Алина", 19)
print("ex2:", person1.say_hello())


# ex3
# Создание нескольких объектов одного класса
class Car:
    def __init__(self, brand):
        self.brand = brand


car1 = Car("Toyota")
car2 = Car("BMW")
car3 = Car("Tesla")

print("ex3:")
print(car1.brand)
print(car2.brand)
print(car3.brand)


# ex4
# Пустой класс с использованием pass
class EmptyClass:
    pass  #нужен чтобы класс не был пустым


empty = EmptyClass()
print("ex4: объект создан ", empty) 