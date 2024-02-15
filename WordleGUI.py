import tkinter as tk

from Board import Board

class WordleGUI:
    def __init__(self, root=None, board=None, guess_callback=None):
        self.root = root if root is not None else tk.Tk() 
        self.board = board if board is not None else Board(self.root)
        self.current_input = [0, 0]
        self.setup_keyboard_input()
        self.guess_callback = guess_callback

    def setup_keyboard_input(self):
        self.root.bind("<Key>", self.handle_key_press)
        # Binding right-click event for each box
        for row in self.board.boxes:
            for box in row:
                box.label.bind("<Button-3>", self.handle_right_click)
        
        
        # Binding left-click event for each box
        for row in self.board.boxes:
            for box in row:
                box.label.bind("<Button-1>", self.handle_left_click)
    
    def handle_key_press(self, event):
        char = event.char.upper()
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and len(char) == 1:
            self.input_letter(char)
        elif event.keysym == 'Return':
            self.submit_guess()
        elif event.keysym == 'BackSpace':
            self.delete_last_character()
    
    def advance_input(self):
        row, col = self.current_input
        if col < 4:  # Check if the current column is less than 4 (since columns are 0-indexed)
            col += 1  # Move to the next column in the current row
        elif col == 4:
            pass
        else:
            raise ValueError(f"Invalid column value at {row, col}.")
        self.current_input = [row, col]  # Update the current input position
    
    def input_letter(self, letter):
        row, col = self.current_input
        if col < 4:  # Ensure no more than 5 letters in a row
            self.board.boxes[row][col].set_text(letter)
            self.advance_input()  # Move to the next box
        elif col == 4:
            if self.board.boxes[row][col].get_text() == "":
                self.board.boxes[row][col].set_text(letter)
            else:
                pass
        else:
            raise ValueError(f"Invalid column value at {row, col} to input letter.")

    def submit_guess(self):
        row = self.current_input[0]
        guess = self.board.get_current_guess(row)
        if len(guess) == 5:
            if self.guess_callback:
                self.guess_callback(guess)
            else:
                # Log a warning or handle the absence of the callback appropriately
                print("Warning: guess_callback is not set.")
            self.current_input = [row + 1, 0]  # Move to the next row
    
    def delete_last_character(self):
        row, col = self.current_input

        # If there's a character in the current column, delete it
        if self.board.boxes[row][col].get_text() != "":
            self.board.boxes[row][col].set_text("")

        # If there's no character in the current column, or if the cursor was at the last column, move back
        elif col > 0:
            col -= 1
            self.board.boxes[row][col].set_text("")

        # Update the cursor position
        self.current_input = [row, col]

    
    def handle_right_click(self, event):
        for row in self.board.boxes:
            for box in row:
                if box.label == event.widget:
                    box.set_text("")  # Clear the text in the box
                    box.set_colour("white")  # Clear the text in the box
                    return
    
    def handle_left_click(self, event):
        for row in self.board.boxes:
            for box in row:
                if box.label == event.widget and box.get_text() != "":
                    box.set_to_next_colour()
                    return

def update_display(self, board, current_attempt):
    # Iterate through each box in the current attempt row and update its display
    for i, box in enumerate(board.boxes[current_attempt]):
        # Assuming each box has a tkinter label assigned to it
        if box.label:
            box.label.config(text=box.get_text(), bg=box.get_colour())




# # Running the GUI for individual testing
# if __name__ == "__main__":
#     gui = WordleGUI()
#     gui.root.mainloop()
