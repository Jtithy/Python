# Author: Tithy
# Date: 2026-07-14
# Description: Write a program to demonstrate person class with name atrribute and talk() method.

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(F"Hello my name's {self.name}")
        

person1 = Person("Tithy")
person1.talk()
person2 = Person("Jane")
person2.talk()
