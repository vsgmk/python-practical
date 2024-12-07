import random as rd
class Test():
    def __init__(self,name,reset):
        self.name=name
        self.reset=reset
        self.test()

    def test(self):
        num=int(input("enter 1 for start test or 0 for not start"))
        marks=0
        while(num==1):  
            if(num==1):
                no=rd.randint(1,9)
                square=no**2
                print("enter square of", no)
                entersquare=int(input())
                
                if(entersquare==square):
                    marks=marks+1
                    num=int(input("enter 1 for continue test or 0 for not continue"))
                else:
                    marks=0
                    num=int(input("enter 1 for continue test or 0 for not continue"))
            else:
                print("your score is 0")
            print("your score is",marks)

name=input("enter your name")
reset=input("enter your recipt id")
Test(name,reset)