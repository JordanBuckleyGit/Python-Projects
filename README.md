# Higher Or Lower Game

This repository contains a Python implementation of the Higher Or Lower card game. In this game, players predict whether the next card drawn from a shuffled deck will be higher or lower than the current card.

## How to Play

### Running the Game
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Navigate to the repository directory in your terminal.
4. Run the command `python higher_or_lower.py` to start the game.

### Gameplay
- Upon starting the game, you will be prompted to select a game mode:
  - **Singleplayer**: Play against the computer.
  - **Stupid Simulation**: Simulate the game with a computer player making random guesses.
  - **Smart Simulation**: Simulate the game with a computer player making intelligent guesses.
- In Singleplayer mode, you will be asked to guess whether the next card will be higher or lower than the current card.
- For Simulation modes, you can choose the number of games to simulate and the type of computer player.

## Code Overview

### `higher_or_lower.py`
- This is the main Python script containing the game logic.
- It includes functions for initializing the game, simulating player guesses, and comparing card values.

### `streakLog*.csv`, `winLog*.csv`
- These files record gameplay statistics, such as streak lengths and wins/losses.
- Separate files are used for different player types: human, stupid computer, and smart computer.

## Contributors
- [JordanBuckleyGit](https://github.com/JordanBuckleyGit)

## License
This project is licensed under the [MIT License](link to license file).
