from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_Sound(self):
     pass

class Lion(Animal):
    def make_Sound(self):
       print("Roar")

class Cat(Animal):
   def make_Sound(self):
      print("Meow")


lion = Lion()
lion.make_Sound()

cat = Cat()
cat.make_Sound()