

with open("log.txt","r") as f:
    lines =f.readlines()

lineno =1
for line in lines:
    if("python" in line):
        print(f"The word python is find in the :{line}")
        break
    lineno+=1
else:
    print("No python is not prenent in any line.")