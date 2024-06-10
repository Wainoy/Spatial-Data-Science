#if statements
a = int(input('enter a number for value a: '))
b = int(input('enter a number for value b: '))
if a>b:
    print(f'{a} is greater than {b}')
elif b>a:
    print(f'{b} is greater than {a}')
else:
    print ('a and b are equal.')