class Demo:
    name = ""

    def __init__(self, name):
        self.name = name

    def fun(self):
        print("My name is "+self.name)

af = Demo("Rambo")
af.fun()
