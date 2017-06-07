class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
    def display_all(self):
        return '{} {} {} {} {}'.format(self.price, self.speed, self.fuel, self.mileage, self.tax)
        return self
emp_1 = Car('$20000','35mph','full', '99mpg', '15%')
emp_2 = Car('$40000', '99mph', 'Kinda full', '7mpg', '15%')
emp_3 = Car('$2000', '30mph', 'empty', '190mpg', '12%')
emp_4 = Car('$10000', '40mph', 'full', '70mpg', '12%')
emp_5 = Car('$1000000','50mph', 'full', '6mpg', '15%')
#print('{}{}'.format(emp_1.first, emp_1.last))
print(emp_1.display_all())
print(emp_2.display_all())
print(emp_3.display_all())
print(emp_4.display_all())
print(emp_5.display_all())
