from TerminalUI import TerminalUI

class HumanPlayer:
    def __init__(self, wordlist, ui=TerminalUI()):
        self.wordlist = wordlist
        self.ui = ui

    def get_guess(self):
        # Get and return user's guess from the terminal
        guess = input("Enter your guess (5-letter word): ").strip().upper()
        while not guess in self.wordlist:
            guess = input("Invalid guess. Enter your guess (5-letter word): ").strip().upper()
        return guess

    def display_board(self, board):
        # Use TerminalUI to display the board
        self.ui.display_board(board)

# Example usage:
# ui = TerminalUI()
# player = HumanPlayer(ui)
# player.display_board(board)  # Where 'board' is an instance of the Board class