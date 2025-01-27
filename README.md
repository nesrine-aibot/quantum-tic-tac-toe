# Quantum Tic-Tac-Toe

### 🚀 Revolutionizing Tic-Tac-Toe with Quantum Computing

This project implements **Tic-Tac-Toe** using **quantum computing** principles, leveraging **Grover's Algorithm** to optimize move selection. It demonstrates how quantum superposition and search optimization can be applied to solve classical problems in innovative ways.

---

## 🌟 Features
- A **quantum board** represented by 9 qubits, each corresponding to a cell on the Tic-Tac-Toe grid.
- Utilizes **Grover's Algorithm** to quickly find the best possible move in a single computation.
- Simulates quantum operations using the **Qiskit** library and the **AerSimulator**.
- Combines quantum computing concepts like **superposition**, **oracle marking**, and **diffusion operators** to revolutionize traditional game logic.

---

## 🛠️ Prerequisites

To run this project, ensure you have the following installed:

- **Python 3.8+**
- **Qiskit** library (Install via `pip install qiskit`)
- **NumPy** library (Install via `pip install numpy`)
- **Qiskit AerSimulator** for quantum simulation

---

## 📜 How It Works

### 1. Quantum Board
- The board is initialized as a quantum register with 9 qubits, each representing a cell.
- Each qubit can be in a **superposition** of states (`|0⟩` and `|1⟩`), allowing all possible moves to be represented simultaneously.

### 2. Grover's Algorithm
- Applies **oracle marking** to identify valid moves (unoccupied cells) and optimal moves based on game logic.
- The **diffusion operator** amplifies the probability of these valid moves, making them the most likely outcomes after measurement.

### 3. Classical Integration
- After quantum computation, the resulting board configuration is measured, collapsing the qubits to a classical state.
- The classical board is updated with the selected move.

### 4. Game Simulation
- The quantum logic is integrated into a playable Tic-Tac-Toe game, alternating turns between Player X and Player O.

---

## 🧑‍💻 Running the Code

1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd quantum-tic-tac-toe
´´´

2. Install dependencies::
   ```bash
    pip install qiskit numpy
´´´

3. Run the game:
   ```bash
   python quantum.py
´´´

## 📂 File Structure

- **`quantum.py`**: Main file containing the implementation of the quantum Tic-Tac-Toe game.
- **`README.md`**: Documentation for the project.

---

## 🧠 Key Quantum Concepts Used

- **Qubits**: Representing the game board in a quantum state.
- **Grover's Algorithm**: For optimizing move selection.
- **Oracle**: Marks valid and optimal moves in the quantum state.
- **Diffusion Operator**: Enhances the probabilities of the correct solutions.
- **Quantum Measurement**: Converts the quantum state to a classical result.

---

## 🤔 Why Quantum Tic-Tac-Toe?

Traditional AI algorithms like **Minimax** take a lot of time to evaluate all possible paths. By using quantum computing:

- We leverage **parallelism** to explore all board configurations simultaneously.
- **Grover's algorithm** optimizes the search, reducing computation time significantly.
- This showcases the power of quantum computing for solving classical problems efficiently.

---

## 🛠️ Future Improvements

- Enhance the oracle to consider deeper strategies for endgame moves.
- Add a graphical interface for better user experience.
- Explore integrating other quantum algorithms for advanced strategy optimization.

---

