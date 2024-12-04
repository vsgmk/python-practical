def zero(a,b): 
    try:
        ans=a/b
    except:
        print(ZeroDivisionError)
    else:
        print("out put is ",ans)
    finally:
        print("it is mendatory perform")
zero(10,5)
