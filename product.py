class Product(object):
    def __init__(self, price, name, weight, brand, cost, status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    def sell(self):
        self.status = 'sold'
        return self
    def addTax(self):
        self.cost = self.cost +(self.cost*0.08)
        return self
    def display_info(self):
        return 'Price: ${} Name: {} Weight: {} Brand: {} Cost: {} Status: {}'.format(self.price, self.name, self.weight, self.brand, self.cost, self.status)
        return self
    def returnitems(self, reason, box):
        self.reason = reason
        self.box = box
        if self.reason == 'defective':
            self.status = 'defective'
            self.price = 0
        if self.box == 'opened':
            self.status = 'used'
            self.price = self.price - (self.price*0.20)
        if self.box == 'unopened':
            self.status = 'like new, for sale'
        return self
shoes = Product(35, 'Shoes', 1, 'Costco', 20, 'unsold')
lamp = Product(45, 'Lamp', 5, 'iKea', 49, 'unsold')
headphones = Product(199, 'Headphones', 1, 'Bose', 150, 'unsold')
shoes.addTax()
shoes.sell()
lamp.addTax()
headphones.addTax()
headphones.sell()
headphones.returnitems('working','opened')
print (shoes.display_info())
print (lamp.display_info())
print (headphones.display_info())
