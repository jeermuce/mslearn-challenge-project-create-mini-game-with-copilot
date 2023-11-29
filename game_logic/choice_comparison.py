def choice_comparison(user, computer, game_state):
    
    if user == computer:
        game_state.update('tie')
        print("It's a tie!")
    elif (user - computer) % 3 == 1:
        game_state.update('win')
        print(f"You are the winner!")
    else:
        game_state.update('loss')
        print(f"Computer is the winner!")
