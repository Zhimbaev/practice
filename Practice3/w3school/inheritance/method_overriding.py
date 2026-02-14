# Ex1 — простое переопределение
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal): #наследует Animal
    def sound(self):
        print("Woof! Woof!")

a = Animal()
d = Dog()

a.sound()  # Some generic animal sound
d.sound()  # Woof! Woof!


# Ex2
class Cat(Animal):
    def sound(self):
        super().sound()  # вызывает метод родителя
        print("Meow!")   # добавляет своё поведение

c = Cat()
c.sound()

print("\n---\n")

# Ex3 
class Vehicle:
    def move(self, speed):
        print(f"Vehicle is moving at {speed} km/h")

class Car(Vehicle):
    def move(self, speed):
        print(f"Car is zooming at {speed} km/h")

v = Vehicle()
c2 = Car()

v.move(50)   # Vehicle is moving at 50 km/h
c2.move(120) # Car is zooming at 120 km/h


# Ex4 
class Employee:
    def calculate_salary(self, base):
        return base

class Manager(Employee):
    def calculate_salary(self, base):
        bonus = 1000
        return base + bonus  # добавляем бонус

e = Employee()
m = Manager()

print(e.calculate_salary(3000))  # 3000
print(m.calculate_salary(3000))  # 4000