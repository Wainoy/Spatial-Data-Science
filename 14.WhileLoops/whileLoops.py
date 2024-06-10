#while loops
#guessing game
secret_number = 199
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input('Enter your 3 lucky numbers: '))
    guess_count += 1
    if guess == secret_number:
        print('Congratulations. You won!')
        break
else:
    print('sorry, You lost.')
