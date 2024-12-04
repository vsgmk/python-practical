class Grandparent:
    def greet(self):
        print("Hello from Grandparent.")

class Parent(Grandparent):
    def welcome(self):
        print("Welcome from Parent.")

class Child(Parent):
    def introduce(self):
        print("Hi from Child.")

child_obj = Child()
child_obj.greet()       # Output: Hello from Grandparent.
child_obj.welcome()     # Output: Welcome from Parent.
child_obj.introduce()   # Output: Hi from Child.
