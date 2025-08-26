# using normal 
def fun():
    n=int(input("Enter the value of n:"))
    r=0
    for i in range(1,n+1):
        r+=i
    return r

print(fun())



# using recursion 

def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
n=int(input("Enter the value of n:"))
print(sum(n))