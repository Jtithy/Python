# Author: Tithy
# Date: 2026-07-14
# Description: Implementing inheritance in Python.
# Inheritance - Mechanism of reusing code of one class into another class.


class Animal:
    def walk(self):
        print("Walk")


class Dog(Animal):
    def bark(self):
        print("Bark")

class Cat(Animal):
    def meow(self):
        print("Meow")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.meow()