my_list= []
class Patients(object):
    def __init__(self, idnum, name, allergies, bednum):
        self.id = idnum
        self.name = name
        self.allergies = allergies
        self.bednum = bednum
class Hospital(object):
    def __init__(self, idnum, name, allergies, bednum):
        self.id = idnum
        self.name = name
        self.allergies = allergies
        self.bednum = bednum
    def add(self, idnum, name, allergies, bednum):
        self.id = idnum
        self.name = name
        self.allergies = allergies
        self.bednum = self.bednum + 1
        print self.bednum
        return self
    def display(self):
        return "ID: {} Name: {}, allergies: {} bednum: {}".format(self.id, self.name, self.allergies, self.bednum)
patient1 = Hospital('100', 'john doe', 'none', 1)
print (patient1.__dict__)
