class TicTacToe():

    def __init__(self):
        self.reset_game()

    def game_board(self):
        b = f'''
Tic-Tac-Toe
 {self.board[0]} | {self.board[1]} | {self.board[2]}
----------- 
 {self.board[3]} | {self.board[4]} | {self.board[5]}
----------- 
 {self.board[6]} | {self.board[7]} | {self.board[8]}
'''
        return b

    def make_move(self, position):
        if position < 0 or position > 8:
            raise ValueError("Input must be between 1 and 9.")
            
        if self.board[position] == '':
            self.board[position] = self.current_player
            winner = self.check_win()
            if winner:
                return winner 
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            raise ValueError("Position already occupied")

    def check_win(self):
        win_conditions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for x, y, z in win_conditions:
            if self.board[x] == self.board[y] == self.board[z] and self.board[x] != '':
                return self.board[x]
        if '' not in self.board:
            return 'Tie'
        
        return None

    def end_game(self, r):
            if r == 'Tie':
                print("The game is a tie!")
            elif r:
                print(f"Player {r} wins!")


    def reset_game(self):
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'

