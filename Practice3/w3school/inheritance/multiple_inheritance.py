
# ex1
class Mother:
    def skills(self):
        print("Cooking, Sewing")

class Father:
    def skills(self):
        print("Gardening, Carpentry")

class Child(Mother, Father): #наследует от отца и матери
    pass

c1 = Child()
c1.skills()  #Cooking, Sewing (Mother comes first)


# ex2
class Mother:
    def cooking(self):
        print("I can cook")

class Father:
    def driving(self):
        print("I can drive")

class Child(Mother, Father):
    pass

c2 = Child()
c2.cooking()  #I can cook
c2.driving()  #I can drive


# ex3
class Mother:
    def skills(self):
        print("Cooking, Sewing")

class Father:
    def skills(self):
        print("Gardening, Carpentry")

class Child(Mother, Father):
    def skills(self):
        print("Programming, Painting")  # override parent methods

c3 = Child()
c3.skills()  #Programming, Painting


# ex4
class Mother:
    def __init__(self):
        print("Mother init called")

class Father:
    def __init__(self):
        print("Father init called")

class Child(Mother, Father):
    def __init__(self):
        super().__init__() 
        print("Child init called")

c4 = Child()
# Mother init called
# Child init called