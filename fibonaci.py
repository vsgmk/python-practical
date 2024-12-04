n=int(input("enter number: "))
a=0
b=1
if(n==0):
    print("0")
elif(n==2 or n==1):
    print("1")
else:
    for i in range(0,n,1):
        c=a+b
        a=b
        b=c
        print(c)
