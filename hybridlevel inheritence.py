# 6.Hybrid Level Inheritance 
class Animal:
    def speaks(self):
        print("Animal can speaks")

class Mammal(Animal):
    def give_birth(self):
        print("Mammals give birth")

class Bird(Animal):
    def lays_egg(self):
        print("Birds gives eggs")

class Access(Mammal,Bird):
    pass

Object=Access()
Object.speaks()
Object.give_birth()
Object.lays_egg()