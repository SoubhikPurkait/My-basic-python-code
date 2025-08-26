

#Factorial using recursion method 
def factorial(n):
    if (n==1 or n==0):
        return 1
    return n* factorial(n-1)

n=int(input("Enter the number to check factorial: "))

print(f"The factorial of {n} is: {factorial(n)} ")



# FActorial using simple for loop  
n=int(input("Enter the number to check factorial: "))
result =1
for i in range (1,n+1):
    result *=i

print(result)
    