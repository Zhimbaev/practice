# class_init_examples.py

# ex1
class Person:
    def __init__(self, name, age):
        self.name = name  # имя человека
        self.age = age  # возраст человека

p1 = Person("Emil", 36)
print("ex1:", p1.name, p1.age)# вывод: Emil 36


# ex2
# __init__ с параметром по умолчанию
class PersonDefault:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p2 = PersonDefault("Emil")
p3 = PersonDefault("Tobias", 25)
print("ex2:", p2.name, p2.age) # Emil 18
print("ex2:", p3.name, p3.age) # Tobias 25


# ex3
# __init__ с несколькими параметрами
class PersonFull:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p4 = PersonFull("Linus", 30, "Oslo", "Norway")
print("ex3:", p4.name, p4.age, p4.city, p4.country)#Linus 30 Oslo Norway


# ex4
# Класс без __init__, свойства задаются после создания объекта
class PersonEmpty:
    pass

p5 = PersonEmpty()
p5.name = "Tobias"
p5.age = 25
print("ex4:", p5.name, p5.age)  #Tobias 25