class employe:
    
    language="bengali"   #This is a cass attribute
    salary=1000000

soubhik=employe()
soubhik.name="Soubhik"   #This is a instance attribute
soubhik.language="Python"   #Overwrite of a instance atttribute over a class attribute
print(soubhik.name,soubhik.language, soubhik.salary)

ani=employe()
ani.name="Aniruddha"
print(ani.name, ani.language, ani.salary)

# Here in the 1st case for soubhik the language is print as python 
# because the python programming language prefer the instance attribute over the class attribute