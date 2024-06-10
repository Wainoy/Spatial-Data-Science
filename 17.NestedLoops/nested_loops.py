
#nested loops
#using a nested for loop to generate a list of coordinates (0,1), (0,2) (1,0) (1,1) and so on.
for x in range(5):
    for y in range (3):
        print(f"({x},{y})") #prints coordinates (0,0) to (4:2)


#Challenge trial
numbers = [5,2,5,2,2]
for number in numbers:
    print('\n', end="")
    for y in range(number):
        print('x', end="")

#solution/example 2
numbers = [2,2,2,2,5]
for number in numbers:
    output = ''
    for count in range(number):
        output += 'x'
    print(output)