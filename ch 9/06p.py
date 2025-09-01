with open("log.txt","r") as f:
    content=f.read()

if ("python" in content):
    print("Yes python is present in the content.")
else:
    print("No pyhotn is not present in the content.")