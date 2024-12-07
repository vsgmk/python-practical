import random as rd
class Shop():
    def __init__(self,owner,brand,opening_date,employs,income):
        self.owner=owner
        self.brand=brand
        self.opening_date=opening_date
        self.employs=employs
        self.income=income
        self.shopno()

    def shopno(self):
        shop=[]
        n=len(shop)
        no=rd.randint(1000,9999)
        for i in range(1,n,1):
            if(i!=shop[i]):
                shop.append(i)
        shop=no
        print("owner name=",owner,"brand=",brand,"opening date=",opening_date,"employs=",employs,"income=",income)
        print("your shop number is: ",owner[0],brand[0],income,shop)


owner=input("enter the name of owner")
brand=input("enter brand of your shop")
opening_date=input("enter date of opening")
employs=int(input("How many employs in your shop"))
income=int(input("how mmuch income you generate from your shop per day"))

Shop(owner,brand,opening_date,employs,income)
