def mul(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
    print("")

n=int(input("Enter the number to print mul table:"))
mul(n)