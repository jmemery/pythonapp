class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self, walk):
        self.walk = walk
        self.health = self.health - 1*walk
        return self
    def run(self, run):
        self.run = run
        self.health = self.health - 5*run
        return self
    def display_health(self):
        return "Your Health is {} ".format(self.health)
        return self
    #def pet(self, pet):
        #self.pet = pet
        #self.health = self.health + 5*pet
        #return self
#dog class
class Dog(Animal):
    def __init__(self):
        self.health = 150
    def pet(self, pet):
        self.pet = pet
        self.health = self.health + 5*pet
    #super(self.health, self),__init__(walk, run)
    #self.health = 150

#Dragon class
class Dragon(Animal):
    def __init__(self):
        self.health = 170
    def fly(self, fly):
        self.health = self.health - 10*fly
        return self
    def display_health(self):
        return "Your Health is {} And you're a Dragon!".format(self.health)
        return self

#my own turtle class!
class Turtle(Animal):
    def __init__(self):
        self.health = 1000
    def lazers(self, lazers):
        self.health = self.health - 110*lazers
        return self
    def display_health(self):
        return "Your health is {}! And youre a Lazer Beam shooting Turtle!!".format(self.health)
        return self

animal = Animal('', 100)     #default animal
dog = Dog()                  #created new dog
cat = Animal('cat', 100)     #test animal
dragon = Dragon()            #created new Dragon
turtle = Turtle()            #created a new lazer shooting turtle
#dog = Dog('dog', 100) `commented out code`

cat.walk(3)
cat.run(7)

#dog pet once run twice walk 3 times

dog.pet(1)
dog.run(2)
dog.walk(3)

#dog.fly(1) #dog class cannot fly
#drangon flys once
dragon.fly(1)

#turtle shoots 2 lazers
turtle.lazers(2)
turtle.walk(3)                  #turtle can also walk and run
turtle.run(18)
print (cat.display_health())     #test animal
print (dog.display_health())
print (dragon.display_health())
print (turtle.display_health())
