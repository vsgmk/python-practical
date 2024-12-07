# import random as rd
# class Student():
#     def __init__(self,name,fathername,surname,DOB,year,cet,en,cast,castcertificatenumber,nationality,aadhar,pan,bank):
#         self.name=name
#         self.fathername=fathername
#         self.surname=surname
#         self.DOB=DOB
#         self.cet=cet
#         self.en=en
#         self.cast=cast
#         self.castcertificatenumber=castcertificatenumber
#         self.nationality=nationality
#         self.aadhar=aadhar
#         self.pan=pan
#         self.bank=bank
#         self.year=year
#         self.prn()
    
#     def admit():
#         if(cet>80):
#             print("you got CSE branch")
#         if(cet>60):
#             print("you got ENTC branch")
#         if(cet>45):
#             print("you got mech branch")
#         if(cet>30):
#             print("you got civil branch")
#         if(cet<30):
#             print("you are extraordinary student...")
        
#         print("congrats...!!!")
#         print("your addmission successfully")

#     def prn():
#         a=[]
#         n=len(a)
#         prn=rd.randint(100000,999999)
#         for i in range(1,n+1,1):
#             if(i!=a[i]):
#                 a.append(a)
#         Student.admit()
#         print("chake your details.")
#         print("your name is: ",name,fathername,surname,"DOB: ",DOB,"Cet marks:",cet,"your EN number is:",en,"cast:",cast,"castcertificatenumber:",castcertificatenumber,"nationality:",nationality,"aadhar:",aadhar,"pan",pan,"Account number",bank)
#         print("your prn number is ",year,cast,prn)
    
# print("welcome in our college...!!!")
# m=int(input("How many student you want to admit..."))
# for i in range(1,m+1,1):
#     name=input("enter name")
#     fathername=input("enter father name")
#     surname=input("enter surname")
#     DOB=input("enter DOB")
#     cet=float(input("enter cet marks"))
#     en=input("enter en id")
#     cast=input("enter cast ex sc,sbc,open")
#     if(cast=="sc"):
#         castcertificatenumber=int(input("enter cast certificate number"))
#     else:
#         castcertificatenumber=0
#     nationality=input("enter domacile number")
#     aadhar=input("enter aadhar number")
#     pan=input("enter pan number")
#     year=int(input("enter addmission date"))
#     bank=int(input("enter bank account number"))
#     Student(name,fathername,surname,DOB,year,cet,en,cast,castcertificatenumber,nationality,aadhar,pan,bank)

import random as rd
class Student():
    def __init__(self,name,fathername,surname,DOB,year,cet,en,cast,castcertificatenumber,nationality,aadhar,pan,bank):
        self.name=name
        self.fathername=fathername
        self.surname=surname
        self.DOB=DOB
        self.cet=cet
        self.en=en
        self.cast=cast
        self.castcertificatenumber=castcertificatenumber
        self.nationality=nationality
        self.aadhar=aadhar
        self.pan=pan
        self.bank=bank
        self.year=year
        self.prn()
    
    def admit():
        if(cet>80):
            print("you got CSE branch")
        if(cet>60):
            print("you got ENTC branch")
        if(cet>45):
            print("you got mech branch")
        if(cet>30):
            print("you got civil branch")
        if(cet<30):
            print("you are extraordinary student...")
        
        print("congrats...!!!")
        print("your addmission successfully")

    def prn(self):
        a=[]
        n=len(a)
        prn=rd.randint(100000,999999)
        for i in range(1,n+1,1):
            if(i!=a[i]):
                a.append(a)
        Student.admit()
        print("chake your details.")
        print("your name is: ",name,fathername,surname,"DOB: ",DOB,"Cet marks:",cet,"your EN number is:",en,"cast:",cast,"castcertificatenumber:",castcertificatenumber,"nationality:",nationality,"aadhar:",aadhar,"pan",pan,"Account number",bank)
        print("your prn number is ",year,cast,prn)
    
print("welcome in our college...!!!")
m=int(input("How many student you want to admit..."))
for i in range(1,m+1,1):
    name=input("enter name")
    fathername=input("enter father name")
    surname=input("enter surname")
    DOB=input("enter DOB")
    cet=float(input("enter cet marks"))
    en=input("enter en id")
    cast=input("enter cast ex sc,sbc,open")
    if(cast=="sc"):
        castcertificatenumber=int(input("enter cast certificate number"))
    else:
        castcertificatenumber=0
    nationality=input("enter domacile number")
    aadhar=input("enter aadhar number")
    pan=input("enter pan number")
    year=int(input("enter addmission date"))
    bank=int(input("enter bank account number"))
    b=Student(name,fathername,surname,DOB,year,cet,en,cast,castcertificatenumber,nationality,aadhar,pan,bank)
    