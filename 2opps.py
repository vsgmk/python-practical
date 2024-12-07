import random as rd
class Group():
    def __init__(self,groupname,members,names,age,weight,email):
        self.groupname=groupname
        self.members=members
        self.names=names
        self.age=age
        self.weight=weight
        self.groupid()

    def groupid(self):
        a=[]
        id=rd.randint(10000,99999)
        n=len(a)        
        for i in range(1,n,1):
            if(id!=a[i]):
                a.append(id)
        print("group name",groupname,"email=",email,"your team id: ",id)

groupname=input("enter your group name: ")
members=int(input("enter how much member in your group: "))
names=input("enter names of members by using comma: ")
age=input("enter ages of team members comma separated")
weight=input("enter weights of members: ")
email=input("enter leader email id")

Group(groupname,members,names,age,weight,email)
