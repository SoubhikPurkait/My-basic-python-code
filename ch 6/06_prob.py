mark=int(input("Enter your mark"))
if(mark<=100 and mark>=90):
    grade="Ex"
elif(mark>=80 and mark<90):
    garde="A"
elif(mark>=70 and mark<80):
    grade="B"
elif(mark>=60 and mark<70):
    grade="C"
else:
    grade="fail"
print(grade)