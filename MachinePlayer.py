import tensorflow as tf
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

class MachinePlayer:
    def __init__(self, wordlist):
        self.wordlist = wordlist

        self.model = self._create_network()

    def _create_network(self):
        # Create a neural network with an 840-neuron input layer and a 5-neuron output layer
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(840, activation='relu'),  # Input layer
            # Add additional hidden layers as needed
            tf.keras.layers.Dense(135, activation='relu'),  # Example hidden layer
            tf.keras.layers.Dense(5, activation='softmax')  # Output layer, 5 neurons for each letter in the guess
        ])
        return model
    
    def is_valid_guess(self, guess, wordlist):
        # Method to determine if the guess is a valid word in the dictionary
        return guess in wordlist

    def generate_guess(self, encoded_board):
        # Feed the encoded board state into the model to get a guess
        model_output = self.model.predict([encoded_board])  # Using model's prediction method
        guess = self.decode_guess(model_output)  # Decoding the output to a word
        return guess

    def interpret_board(self, board):
        # Encoding the board state
        encoded_board = self._encode_board(board)
        return encoded_board

    def _encode_board(self, board):
        # Encoding logic as previously defined
        color_encoding = {'white': 0, 'grey': 1, 'yellow': 2, 'green': 3}
        encoded_board = []

        for row in board.boxes:
            for box in row:
                letter_encoded = [0] * 27
                if box.get_text():
                    index = ord(box.get_text()) - 65
                    letter_encoded[index] = 1
                else:
                    letter_encoded[-1] = 1

                color_encoded = color_encoding[box.get_colour()]
                encoded_board.extend(letter_encoded + [color_encoded])

        return encoded_board

    def decode_guess(self, output):
        # Decoding the output into a word
        decoded_word = self._decode_output(output)
        return decoded_word

    def _decode_output(self, output):
        # Convert output probabilities to characters
        decoded_word = ''
        for prob in output:
            letter_index = prob.index(max(prob))
            if letter_index < 26:
                decoded_word += chr(letter_index + 65)
            else:
                decoded_word += ' '  # Blank space for non-letter

        return decoded_word

    def calculate_reward(self, feedback, guess):
        # Calculate the reward based on the feedback
        reward = 0
        if not self.is_valid_guess(guess):
            reward -= 20  # Penalty for invalid guess
        else:
            for color in feedback:
                if color == 'green':
                    reward += 10
                elif color == 'yellow':
                    reward += 5
                elif color == 'grey':
                    reward += 0
                else:  # Blank
                    reward += 1
        return reward
    
################################################################################################

from Board import Board

if __name__ == "__main__":
    wordlist = ["HELLO", "WORLD", "TESTS", "PYTHON"]
    machine_player = MachinePlayer(wordlist)

    # Create a dummy board for testing
    dummy_board = Board()
    dummy_board.update_board("HELLO", ["green", "yellow", "grey", "white", "white"], 0)

    # Interpret the board
    encoded_board = machine_player.interpret_board(dummy_board)

    # Example model output (placeholder)
    model_output = [[0.1]*26 + [0.9], [0.1]*26 + [0.9], [0.1]*26 + [0.9], [0.1]*26 + [0.9], [0.1]*26 + [0.9]]

    # Decode the guess
    decoded_guess = machine_player.decode_guess(model_output)

    # Print the results for demonstration
    print("Encoded Board:", encoded_board)
    print("Decoded Guess:", decoded_guess)