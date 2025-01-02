class TicTacToe:
    def __init__(self):
        # Start a new game
        self._board = [[' '] * 3 for j in range(3)]
        self._player = 'X'

    # Method allows the current player to place a mark ('X' or 'O') at a specified position (i, j) on the board
    def mark(self, i, j):
        # Checks if the indices i and j are valid (between 0 and 2). 
        # If not, it raises a ValueError indicating an invalid position
        if not (0<=i<=2 or 0<=j<=2):
            raise ValueError('Invalid Board Position')
        # Ensures the selected board position is empty. 
        # If not, it raises an error saying the position is already occupied
        if self._board[i][j] != ' ':
            raise ValueError('Board position already occupied')
        # Calls the winner method to check if the game is already over. 
        # If a winner exists, a ValueError is raised indicating the game is complete
        if self.winner() is not None:
            raise ValueError('Game completed...')
        
        # After placing a mark, this toggles the player: if the current player was 'X', it switches to 'O', and vice versa
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    # This private helper method checks if a given player (mark, either 'X' or 'O') has won the game
    def _is_win(self, mark):
        board = self._board

        # Check whether the board configuration is a win for any given player
        # Evaluates to True if any of the following conditions are met
        return (mark == board[0][0] == board[0][1] == board [0][2] or
                mark == board[1][0] == board[1][1] == board [1][2] or
                mark == board[2][0] == board[2][1] == board [2][2] or
                mark == board[0][0] == board[1][0] == board [2][0] or
                mark == board[0][1] == board[1][1] == board [2][1] or
                mark == board[0][2] == board[1][2] == board [2][2] or
                mark == board[0][0] == board[1][1] == board [2][2] or
                mark == board[0][2] == board[1][2] == board [2][0])

    # This method checks if there is a winner.
    def winner(self):
        for mark in 'XO': # Loops through each player mark, 'X' and 'O'
            if self._is_win(mark): # Uses the _is_win helper method to check if either player has won
                return mark
            else:
                return None
    
    # This method defines how the board is printed
    def __str__(self):
        # Iterates over each row of the board (self._board[r]) and joins the row elements with a vertical bar ('|')
        rows = ['|'.join(self._board[r]) for r in range(3)]
        # Joins each row string with horizontal dividers ('-----') to visually separate the rows, making the board appear in a Tic-Tac-Toe grid format
        return '\n-----\n'.join(rows)
    
game = TicTacToe()

game.mark(1, 1); game.mark(0,2)
game.mark(2,2); game.mark(0,0)
game.mark(0,1); game.mark(2,1)
game.mark(1,2); game.mark(1,0)
game.mark(2,0)

print(game)
winner = game.winner()
if winner is None:
    print('It is a tie ladies and gentlemen')
else:
    print(winner, ' has won the game. Congratulations!')
