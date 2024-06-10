#inheritance
class Mammal:
     def walk(self):
         print('walk')
class Cat(Mammal): #inheritance
    def be_awesome(self):
        print("awesome")
class Dog(Mammal):
    pass


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.be_awesome()


