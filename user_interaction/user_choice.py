def user_choice():
    user_input = input(
        'Enter 0 for rock, 1 for scissors, 2 for paper, q to quit:'
    )
    user_input = user_input.lower()
    if user_input == '0':
        print('You chose rock.')
        return int(user_input)
    elif user_input == '1':
        print('You chose scissors.')
        return int(user_input)
    elif user_input == '2':
        print('You chose paper.')
        return int(user_input)
    elif user_input == 'q':
        print('Goodbye!')
        exit()
    else:
        print('Invalid input, try again or quit.')
        return user_choice()
