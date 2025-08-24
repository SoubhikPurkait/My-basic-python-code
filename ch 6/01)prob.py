a1=int(input("Enter the 1st number:"))
a2=int(input("Enter the 2nd number:"))
a3=int(input("Enter the 3rd number:"))
a4=int(input("Enter the 4th number:"))

if(a1>a2 and a1>a3 and a1>a4):
    print("The greater value is a1",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("The greater value is a2",a2)
if(a3>a2 and a3>a1 and a3>a4):
    print("The greater value is a3",a3)
if(a4>a2 and a4>a3 and a4>a1):
    print("The greater value is a4",a4)