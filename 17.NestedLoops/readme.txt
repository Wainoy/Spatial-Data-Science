an example of how to use nested for loops to generate and print a list of coordinates.
to generate a list of coordinates using a nested loop:

for number in range(4):
    print(number)
    for count in range(3):
        print(f"({number},{count})")