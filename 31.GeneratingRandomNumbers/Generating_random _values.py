#Generating random values
import random
for i in range(3):
    print(random.random()) #returns a random number between 0 and 1 for each iteration
    print (random.randint(10,20)) #returns a random integer between 10 and 20 for each iteration

#to randomly select a leader from a team
team = ['James', 'John', 'Andrew','Jane', 'Eve']
leader = random.choice(team)
print(leader)


#Exercise: define a class Dice with a method 'roll' that returns a tuple of results displayed afer rolling two dice
#trial
import random
values = (1, 2, 3, 4, 5, 6)
class Dice:
    def __init__(self, values):
        self.values = values
    def roll(self):
        print(f'your score is {self.values}')


dice1 = Dice(random.choice(values))
dice1.roll()

#solution
import random
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        return first,second

dice1 = Dice()
print(dice1.roll())