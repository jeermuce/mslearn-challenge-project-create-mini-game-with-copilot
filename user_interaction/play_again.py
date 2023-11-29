def play_again(game_state):
    user_input = input('Play again? (y/n): ')
    # lowercase the input

    if user_input == 'y':
        return True
    elif user_input == 'n':
        game_state.print_stats()
        return False
    else:
        print('Invalid input, try again.')
        return play_again(game_state)
