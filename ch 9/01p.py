f=open("poem.txt")
c=f.read()
if("twinkle" in c ):
    print("The word twinkle is present the poem ")
else:
    print("the word twinklw is not present in the poem ")

f.close()