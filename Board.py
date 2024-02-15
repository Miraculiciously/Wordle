from Box import Box

class Board:
    def __init__(self):
        self.boxes = [[Box() for _ in range(5)] for _ in range(6)]

    def update_board(self, guess, evaluation, row):
        for i, char in enumerate(guess):
            self.boxes[row][i].set_text(char)
            self.boxes[row][i].set_colour(evaluation[i])
