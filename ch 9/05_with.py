f=open("file.txt")
data=f.read()
print(data)
f.close()

#this same code is written by using the with statement,.where we don't need to write the "f.close()" dstatement to close the existing file 

with open("file.txt") as f:
    print(f.read())