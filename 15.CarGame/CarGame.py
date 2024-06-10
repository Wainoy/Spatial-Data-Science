command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car already started')
        else:
            started = True
            print('Car started. Ready to go.')
    elif command == 'stop':
        if not started:
            print('Car already stopped')
        else:
            started = False
            print('Car stopped')
    elif command == 'help':
        print('''start - to start the car \n stop - to stop the car \n quit - to quit''')
    elif command == 'quit':
        break
    else:
        print('Invalid option')