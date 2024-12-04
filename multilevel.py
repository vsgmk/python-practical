class Animal:
    def sound(self):
        print("Animal sounds")

class Bird(Animal):
    def fly(self):
        print("I can fly")

class Human(Animal):
    def move(self):
        print("I can walk..")

obj=Human()
obj1=Bird()
obj.move()
obj.sound()
obj1.fly()
obj1.sound()
