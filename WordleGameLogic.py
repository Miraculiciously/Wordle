class WordleGameLogic:
    def __init__(self, correct_word, wordlist):
        self.correct_word = correct_word
        self.wordlist = wordlist
        self.max_attempts = 6
        self.current_attempt = 0
        self.game_over = False
        self.win_status = None
    
    def is_valid_guess(self, guess):
        return len(guess) == 5 and guess.isalpha() and guess in self.wordlist

    def evaluate_guess(self, guess):
        if not self.is_valid_guess(guess):
            # Handle invalid guess scenario
            NotImplemented
        else:
            result = ['grey'] * len(guess)  # Initialize all to grey
            correct_word_temp = list(self.correct_word)

            # First pass for green
            for i in range(len(guess)):
                if guess[i] == self.correct_word[i]:
                    result[i] = 'green'
                    correct_word_temp[i] = None  # Mark as used

            # Second pass for yellow
            for i in range(len(guess)):
                if guess[i] in correct_word_temp and result[i] != 'green':
                    result[i] = 'yellow'
                    correct_word_temp[correct_word_temp.index(guess[i])] = None

            # Increment attempt and determine if game is over
            self.current_attempt += 1
            game_over = self.current_attempt >= self.max_attempts or guess == self.correct_word
            return result, game_over

def check_game_status(self, board):
    # Check if the last row on the board contains the correct word
    if self.current_attempt > 0:
        last_row = board.boxes[self.current_attempt - 1]
        last_guess = ''.join([box.get_text() for box in last_row])
        if last_guess == self.correct_word:
            self.win_status = True
            self.game_over = True
            return

    # Check if the maximum number of attempts has been reached
    if self.current_attempt >= self.max_attempts:
        self.win_status = False
        self.game_over = True
        return

    # If neither condition is met, the game is not over
    self.game_over = False


    # def update_game_state(self, guess, evaluation):
    #     # Update the boxes in the board with the guess and evaluation
    #     for i, (letter, eval_result) in enumerate(zip(guess, evaluation)):
    #         self.board.boxes[self.current_attempt][i].set_text(letter)
    #         self.board.boxes[self.current_attempt][i].set_colour(eval_result)  # Assuming a method to set color

    #     # Update current attempt and check for game over
    #     self.current_attempt += 1
    #     self.game_over = self.is_game_over()


# if __name__ == "__main__":
#     correct_word = "ABBAU"  # Example correct word
#     wordlist = ["ABBAU", "ALIEN"]  # Example wordlist
#     player = HumanPlayer()
#     game = WordleGameLogic(correct_word, player, wordlist)
#     game.run_game()