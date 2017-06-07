class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = true
    def login(self):
        self.logged = true
        print self.name
        return self
    def logout(self):
        self.logged = false
        print self.name + "is not logged in"
        return self
    def show(self):
        print "my name is {}. You can email me at {}.".format(self.name, self.email)
        return self
