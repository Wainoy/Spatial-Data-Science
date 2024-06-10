#Comparison Operators
#Sample Exercise 6: A program to input the name of a user. the name should be between 3 and 50 characters
name = input('Your name: ')
if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) >50:
    print('Name cannot be longer than 50 characters')
else:
    print(f'You have a great name, {name}')
