class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def createEmail(self):
        email=self.name + str(self.age) + '@gmail.com'
        print(email)

st1=Student('vince', 40)
print(st1.name)
print(st1.age)
st1.createEmail()