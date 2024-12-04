n=int(input("enter number"))
flag=0
if(n==1):
    print(n,"is not prime number")
else:
    for i in range(2,n,1):
        if(n%i==0):
            flag=1
            break
    if(flag==0):
        print(n,"is prime number")
    else:
        print(n,"is not a prime number")
    