# Number Guessing Game

## Overview
The Number Guessing Game is a simple command-line interface (CLI) game where the computer randomly selects a number between 1 and 100, and the player must guess it within a limited number of attempts based on the selected difficulty level.

## Features
- Randomly generates a number between 1 and 100
- Allows players to select a difficulty level:
  - Easy (10 chances)
  - Medium (5 chances)
  - Hard (3 chances)
- Provides hints on whether the guessed number is too high or too low
- Tracks the number of attempts
- Displays time taken to guess the number
- Option to play multiple rounds
- Keeps track of the high score (fewest attempts needed to win)

## Installation
1. Clone the repository or download the script.
   ```sh
   git clone <repository-url>
   cd number_guessing_game
   ```
2. Ensure you have Python installed (Python 3.x recommended).
3. No external libraries are required as it uses Python's built-in modules.

## Usage
Run the script using Python:
```sh
python number_guessing_game.py
```

### Example Gameplay
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2
Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 30
Congratulations! You guessed the correct number in 2 attempts.
```

## File Structure
- `number_guessing_game.py` - Main game script

## Error Handling
- Ensures valid numeric input
- Handles incorrect difficulty selections
- Prevents invalid guesses (e.g., out of range numbers)

## Future Improvements
- Add a hint system to give clues after multiple wrong attempts
- Implement multiplayer mode
- Save high scores to a file for persistence

## License
This project is open-source and available under the MIT License.

## Contributors
Developed by Vamsi Krishna Sirivela. Contributions are welcome!

## Roadmap
For a detailed roadmap of this project, visit: https://roadmap.sh/projects/number-guessing-game

