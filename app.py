from game_logic.game_state import GameState
from user_interaction.user_choice import user_choice
from user_interaction.play_again import play_again
from game_logic.random_choice import random_choice
from game_logic.choice_comparison import choice_comparison


def main():
    game_state = GameState()
    while True:
        user = user_choice()
        computer = random_choice()
        choice_comparison(user, computer, game_state)
        if not play_again(game_state):
            break

main()
