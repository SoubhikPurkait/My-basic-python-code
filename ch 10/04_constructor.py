class employe:
    
    language="bengali"   #This is a cass attribute
    salary=1000000

    def __init__(self):
        print("Here i am creating a object")

soubhik=employe()
soubhik.name="Soubhik"   #This is a instance attribute
print(soubhik.name,soubhik.language, soubhik.salary)

ani=employe()
ani.name="Aniruddha"
print(ani.name, ani.language, ani.salary)