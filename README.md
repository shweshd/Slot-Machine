# 🎰 Python Slot Machine

A simple command-line **slot machine game built with Python**. The project demonstrates fundamental Python concepts such as functions, loops, dictionaries, lists, random selection, input validation, and basic game logic.

## Features

* Deposit an initial balance
* Choose how many lines to bet on
* Place a bet on each selected line
* Randomly generate a 3×3 slot machine
* Different symbols have different probabilities and payout values
* Check winning lines
* Calculate winnings and total bets
* Display the current balance
* Continue playing until the user quits
* Validate user input and betting limits

## How the Game Works

The slot machine uses four symbols:

| Symbol | Count | Value |
| ------ | ----: | ----: |
| A      |     2 |    $5 |
| B      |     4 |    $4 |
| C      |     6 |    $3 |
| D      |     8 |    $2 |

The more frequently a symbol appears in the symbol pool, the more likely it is to be selected.

The game has:

* **3 rows**
* **3 columns**
* Maximum **3 betting lines**
* Minimum bet: **$1**
* Maximum bet: **$100**

## Example

```text
What would you like to deposit? $100

Current balance is $100
Press enter to play (q to quit).

Enter the number of lines to bet on (1-3)? 3
What would you like to bet on each line? $10

You are betting $10 on 3. Total bet is equal to: $30

A | B | D
A | B | C
A | B | D

You won $150.
You won on lines: 1

Current balance is $220
```

## Project Structure

```text
slot-machine/
│
├── main.py
└── README.md
```

## Requirements

* Python 3.x
* No external Python libraries are required.

The project uses Python's built-in `random` module.

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project

```bash
cd slot-machine
```

### 3. Run the program

```bash
python main.py
```

On some systems, you may need:

```bash
python3 main.py
```

## Main Functions

### `deposit()`

Gets the starting balance from the user and validates that the amount is greater than zero.

### `get_number_of_lines()`

Asks the user how many lines they want to bet on and ensures the number is between 1 and 3.

### `get_bet()`

Gets the betting amount for each line and checks that it is between the minimum and maximum bet.

### `get_slot_machine_spin()`

Creates the random 3×3 slot machine using the available symbols.

### `print_slot_machine()`

Displays the generated slot machine in a readable format.

### `check_winnings()`

Checks whether the selected betting lines contain matching symbols and calculates the winnings.

### `spin()`

Controls one complete round of the game:

1. Get the number of lines.
2. Get the bet.
3. Check the balance.
4. Generate the slot machine.
5. Check winnings.
6. Calculate the result.

### `main()`

Runs the main game loop and allows the player to continue playing or quit.

## Concepts Practiced

This project helped practice:

* Variables and constants
* Dictionaries
* Lists
* `for` loops
* `while` loops
* Functions
* Function parameters and return values
* `if / elif / else`
* Input validation
* String formatting
* List copying and removal
* The `random` module
* Nested loops
* Basic game logic

## Future Improvements

Possible improvements include:

* Add more symbols
* Add different winning combinations
* Add diagonal winning lines
* Add animations
* Add colored terminal output
* Add a betting history
* Add a maximum number of spins
* Add sound effects
* Add a graphical interface using Tkinter
* Save the player's balance between sessions

## Author

**Shwesh Dubey**

This project was created as part of my Python learning and practice projects.
