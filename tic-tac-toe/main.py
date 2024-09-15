import os
from game import TicTacToe

# functions
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def play_again():
    while True:
        try:
            reset = int(input(play_again_txt))
            if reset == 1:
                game.reset_game()
                clear_terminal()
                print(game.game_board())
                return True
            elif reset == 2:
                print('\nGoodbye...\n')
                return False
            else:
                print('Input a valid number (1, 2).')
        except ValueError:
            print('Input a valid number (1, 2).')

# txt
play_again_txt = '''
Play Again?
1. Yes
2. No
'''

instructions_txt = '''
Which position do you want to play? 0 to 8
Row 1: 1 | 2 | 3
Row 2: 4 | 5 | 6
Row 3: 7 | 8 | 9
'''
#import TicTacToe
game = TicTacToe()

# initial
print(game.game_board())
print(instructions_txt)

# game
def main():
    while True:
        try:
            user_input = int(input('Choose a position (1-9): ')) - 1
            result = game.make_move(user_input)
            clear_terminal()
            print(game.game_board())

            if result:
                game.end_game(result)
                if not play_again():
                    break

        except ValueError as e:
            clear_terminal()
            print(game.game_board())
            if 'invalid literal' in str(e):
                print("Invalid input. Please enter a number between 1 and 9.")
            else:
                print(f"{e}")

if __name__ == "__main__":
    main()