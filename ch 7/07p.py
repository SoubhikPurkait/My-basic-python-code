n=int(input("Enter the no of row : "))
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(i*2-1), end="")
    print("")