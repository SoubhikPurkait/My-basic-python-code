class employe:
    
    language="bengali"   #This is a cass attribute
    salary=1000000

    def getinfo(self):
        print(f"Here the language is {self.language} and the salary is {self.salary}")

soubhik=employe()
soubhik.name="Soubhik"   #This is a instance attribute
# print(soubhik.name,soubhik.language, soubhik.salary)
soubhik.getinfo()

# ani=employe()
# ani.name="Aniruddha"
# print(ani.name, ani.language, ani.salary)