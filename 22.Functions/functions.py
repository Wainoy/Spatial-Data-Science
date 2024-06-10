#functions
def greet_user(firstName, lastName):
    print(f'Hello {firstName}')
    print('How are you doing')
print('Start of the function')
greet_user("Eve","Nyawira") #'Eve' and 'Nyawira' are positional arguments
greet_user(lastName="Nyawira", firstName = 'Eve') #keyword arguments
print('The End')
