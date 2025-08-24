mark1=int(input("Enter the 1st number:"))
mark2=int(input("Enter the 2nd number:"))
mark3=int(input("Enter the 3rd number:"))

total_percentage=(100*(mark1+mark2+mark3))/300
if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You are pass:",total_percentage)
else:
    print("you failed, better luck next time:",total_percentage)