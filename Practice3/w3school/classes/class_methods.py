#ex1
class Playlist:
    def __init__(self, name):
        self.name= name #название плейлиста
        self.songs = [] #создаем список в котором будет хранить песни

    def add_song(self, song):
        self.songs.append(song) # добавляем песню
        print(f"Added song:{song}")

    def remove_song(self, song):
        if song in self.songs: #проверка песни в списке
            self.songs.remove(song)
            print(f"Removed:{song}")
            return True # возвраащет значение True, return необяз, просто для демонстрации
        return False #если не найдена false

    def show_songs(self):
        print(f"Playlist: '{self.name}':")
        for x in self.songs:
            print(x, end = ' ')
        
a = Playlist("Favourite")
a.add_song("Bethoven")
a.add_song("Black")
a.add_song("Rule")
a.add_song("Goodie")

a.remove_song("Black")
a.show_songs()

#ex2
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil") 

del Person.greet
"""
p1.greet() # This will cause an error 
"""
# ex3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)  # Tobias (36)


# ex4
class Calculator:
    def __init__(self, number):
        self.number = number

    def add(self, value):
        self.number += value

    def multiply(self, value):
        self.number *= value

    def display(self):
        print(f"Current number: {self.number}")


# Test ex4
calc = Calculator(10)
calc.add(5)        # 10 + 5
calc.multiply(2)   # 15 * 2
calc.display()     # 30