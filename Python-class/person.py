
class Person:
    def __init__(self, name, age):
        self.name=name  
        self.age=age


p1=Person('Vince',40)
print(p1.name)
print(p1.age)

print('The name and age are {} and {} respectively'.format(p1.name,p1.age))