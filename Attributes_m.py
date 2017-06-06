
class Bike(object):
    def __init__(self, name, price, maxspeed, miles=0):
        self.name = name
        self.price = price
        self.maxspeed = maxspeed
        self.miles = miles
    def display_info(self):
        print price
        print maxspeed
        print miles
    def ride(self,miles):
        print "Riding"
        miles = miles + 10
        print miles
    def reverse(self, miles):
        print "Reversing"
        miles = miles - 5
        print miles
        display_info(bike3)
bike1 = Bike(Bike, 200, "25  mph")
bike2 = Bike(Bike, 350, "33 mph")
bike3 = Bike(Bike, 150, "88 mph")
