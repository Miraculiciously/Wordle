from Board import Board
from WordleGameLogic import WordleGameLogic
from HumanPlayer import HumanPlayer
# from MachinePlayer import MachinePlayer

import random
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def load_wordlist(filename):
    with open(filename, 'r') as file:
        return [line.strip().upper() for line in file]

def main():
    wordlist = load_wordlist("dict.txt")
    correct_word = random.choice(wordlist)
    print(correct_word)
    board = Board()
    game_logic = WordleGameLogic(correct_word, wordlist)
    player = HumanPlayer()  # Default UI is TerminalUI

    while not game_logic.game_over:
        player.display_board(board)
        guess = player.get_guess()
        result, game_over = game_logic.evaluate_guess(guess)

        if result:
            current_row = game_logic.current_attempt - 1  # current_attempt is already incremented
            board.update_board(guess, result, current_row)  # Pass current row to update_board
            game_logic.game_over = game_over

        player.display_board(board)  # Display updated board

        if game_logic.game_over:
            # Handle end-of-game scenario
            message = "Congratulations, you won!" if game_logic.win_status else "Game over. Better luck next time!"
            player.ui.display_message(message)
            # Additional logic for replay or exit can be added here


if __name__ == "__main__":
    main()
