callnum = 1
x = [0]
class Call(object):
    def __init__(self, idn, name, phone, time, reason):
        self.id = idn
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
    def display(self):
        return "Your ID: {} " "| Name of Caller: {} " "|Phone Number: {} " "| Time of Call: {} " "| Reason for Call: {} ".format(self.id, self.name, self.phone, self.time, self.reason)
        return self
    def get_list(self):
        return display
    def add(self, idn, name, phone, time, reason):
        self.id = idn
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
        x.append(self.idn, self.name, self.phone, self.time, self.reason)
        return self
class CallCenter(Call):
    def __init__(self):
        self.id = 1 + callnum
    def calls(self):
        print Call(object)
        return self
    def add(self, idn, name, phone, time, reason):
        self.id = idn
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
        x.append(self.idn, self.name, self.phone, self.time, self.reason)
        return self

call = Call(1000, "john doe", 3107778989, '16:20', 'internet is down')
call2 = Call(1001, "Jane Doe", 322434356, '17:50', 'computer crashed')
call3 = Call.add(1002, "Jane Doe", 322434356, '17:50', 'computer crashed')
print(call.display())
print(call2.display())
print x
