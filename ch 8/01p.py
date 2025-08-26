def gretest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("enter the value of c: "))

print(gretest(a,b,c))