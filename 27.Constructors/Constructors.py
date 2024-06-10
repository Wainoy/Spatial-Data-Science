#Constructors
class Point:
    def __init__(self,x,y): #a constructor
        self.x = x
        self.y = y
    def move(self):
        print('move')
    def draw(self):
        print('draw')

point1 = Point(10,20)
point1.x = 11
print(point1.x)


#Sample Exercise
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi, My name is {self.name}')


person1 = Person('Eve')
print(person1.name)
person1.talk()

person2 = Person('Bob')
person2.talk()


class Cat:
    def __init__(self,discipline): #a constructor
        self.discipline = discipline


ash = Cat('naughty cat')
print(ash.discipline)