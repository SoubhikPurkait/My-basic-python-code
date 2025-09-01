class calculator():
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The square of the given number is {self.n*self.n}")
    def cube(self):
        print(f"The square of the given number is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The square of the given number is {(self.n)**0.5}")


a=calculator(12)

a.square()
a.cube()
a.squareroot()