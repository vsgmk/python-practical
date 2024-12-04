def arm(n):
    m=n
    sum=0
    b=str(n)
    for i in range(0,len(b),1):
        rem=n%10
        sum=sum+rem**len(b)
        n=n//10
    if(sum==m):
        print("given number is armstrong")
    else:
        print("not armstrong")
n=int(input("enter number "))
arm(n)
