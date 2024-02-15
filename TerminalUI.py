class TerminalUI:
    def display_board(self, board):
        for row in board.boxes:
            row_display = ' '.join([self.format_box(box) for box in row])
            print(row_display)
        print()  # Print an empty line for better separation

    def format_box(self, box):
        # Mapping from color names to ANSI escape codes for foreground color
        color_codes = {
            'green': '\033[32m',  # Green
            'yellow': '\033[33m', # Yellow
            'grey': '\033[37m',   # White (for grey representation)
            'white': '\033[37m'   # White
        }
        color_code = color_codes.get(box.colour, '\033[37m')  # Default to white if color not found
        return f"{color_code}{box.text}\033[0m"  # \033[0m resets the color

    def display_message(self, message):
        print(message)
