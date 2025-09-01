class Employe:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

e1=Employe("soubhik",120000,713404)
print(e1.name,e1.salary,e1.pin,e1.company)
e2=Employe("Moon",10000,725000)
print(e2.name,e2.salary,e2.pin,e2.company)