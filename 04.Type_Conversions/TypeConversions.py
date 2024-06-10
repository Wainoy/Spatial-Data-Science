#Type Conversion
weight = int(input('Your weight: '))
units = input('(l)bs or (k)g: ')
if units.upper() == 'L':
    weight = weight*0.452
    print(f'Your are {weight} kg')
if units.upper() == 'K':
    weight = weight * 2.204
    print(f'Your are {weight} lbs')
