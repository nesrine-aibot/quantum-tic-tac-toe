import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from math import pi, sqrt


class QuantumTicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize an empty board

    def print_board(self):
        """Print the current board state."""
        print("\nCurrent board:")
        for i in range(3):
            print(" | ".join(self.board[i * 3:(i + 1) * 3]))
            if i < 2:
                print("-" * 5)

    def is_valid_move(self, pos):
        """Check if a move is valid."""
        return 0 <= pos < 9 and self.board[pos] == ' '

    def apply_move(self, pos, player):
        """Apply a move to the board."""
        self.board[pos] = player

    def evaluate_board(self):
        """Check for a win, loss, or draw."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return 1 if self.board[combo[0]] == 'X' else -1
        return 0 if ' ' not in self.board else None

    def oracle(self, qc, qubits, valid_moves):
        """
        Define the Grover oracle to mark valid states (unoccupied positions on the board).
        """
        for move in valid_moves:
            binary_move = format(move, f'0{len(qubits)}b')
            for i, bit in enumerate(binary_move):
                if bit == '0':
                    qc.x(qubits[i])

            qc.h(qubits[-1])
            qc.mcx(qubits[:-1], qubits[-1])
            qc.h(qubits[-1])

            for i, bit in enumerate(binary_move):
                if bit == '0':
                    qc.x(qubits[i])

    def diffusion_operator(self, qc, qubits):
        """
        Apply Grover's diffusion operator to amplify marked states.
        """
        qc.h(qubits)
        qc.x(qubits)
        qc.h(qubits[-1])
        qc.mcx(qubits[:-1], qubits[-1])
        qc.h(qubits[-1])
        qc.x(qubits)
        qc.h(qubits)

    def find_best_move(self):
        """
        Use Grover's algorithm to find the best move for the current board state.
        """
        num_qubits = 4  # We need only enough qubits to represent 0-8 (3 qubits minimum, 4 for flexibility)
        qr = QuantumRegister(num_qubits, name='q')  # Quantum register
        cr = ClassicalRegister(num_qubits, name='c')  # Classical register
        qc = QuantumCircuit(qr, cr)

        # Step 1: Initialize qubits in a uniform superposition
        qc.h(qr)

        # Step 2: Apply the Grover oracle
        valid_moves = [i for i in range(9) if self.is_valid_move(i)]
        if not valid_moves:
            raise ValueError("No valid moves available!")
        self.oracle(qc, qr, valid_moves)

        # Step 3: Apply the diffusion operator
        self.diffusion_operator(qc, qr)

        # Step 4: Measure the qubits
        qc.measure(qr, cr)

        # Step 5: Simulate the quantum circuit
        simulator = AerSimulator()
        result = simulator.run(qc, shots=1024).result()
        counts = result.get_counts()

        # Find the most probable state and convert it to a move
        valid_counts = {int(state, 2): count for state, count in counts.items() if int(state, 2) in valid_moves}
        if not valid_counts:
            raise ValueError("No valid moves found in the result!")

        best_move = max(valid_counts, key=valid_counts.get)
        return best_move

    def play_game(self):
        """
        Simulate a game of Tic-Tac-Toe with Player X using Grover's algorithm.
        """
        current_player = 'X'
        while True:
            self.print_board()
            print(f"Player {current_player}'s turn.")

            if current_player == 'X':
                # Use Grover's algorithm to find the best move
                try:
                    best_move = self.find_best_move()
                except ValueError as e:
                    print(str(e))
                    print("Game over!")
                    break
            else:
                # For simplicity, Player O plays randomly
                valid_moves = [i for i in range(9) if self.is_valid_move(i)]
                best_move = np.random.choice(valid_moves)

            if self.is_valid_move(best_move):
                self.apply_move(best_move, current_player)
            else:
                print(f"Invalid move by {current_player}.")
                continue

            # Check for game result
            result = self.evaluate_board()
            if result == 1:
                self.print_board()
                print("Player X wins!")
                break
            elif result == -1:
                self.print_board()
                print("Player O wins!")
                break
            elif result == 0:
                self.print_board()
                print("It's a draw!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'


# Run the game
if __name__ == '__main__':
    game = QuantumTicTacToe()
    game.play_game()
