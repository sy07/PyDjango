class Car:
    def brand(self):
        print("This is car")

class Chevy(Car):
    #override
    def brand(self):
        print("This is Chevrolet Camaro")

obj = Chevy()
obj.brand()
