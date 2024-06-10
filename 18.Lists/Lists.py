#lists
names = ['Eve', 'Charles', 'Gabriel', 'Wainoy','Terry']
print(names)
print(names[-1])
print (names[:-1]) #doesn't print Terry
print(names[2:]) #prints Gabriel, Wainoy and Terry
print(names[0:7]) #prints all the names

#Exercise trial
#write a program to find the largest number in a list
numbers = [1,2,3,4,76,345,646]
print(max(numbers))

#exercise solution
numbers = [1,2,3,4,76,345,646]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print (f'maximum number in {numbers} is {max}')