# 🎰 Python Slot Machine

A simple **slot machine game built with Python and CustomTkinter**. The project demonstrates fundamental Python concepts such as functions, loops, dictionaries, lists, random selection, input validation, object-oriented programming, and basic game logic through a graphical user interface.

## Features

* 💰 Deposit an initial balance
* 🎯 Choose how many lines to bet on
* 💵 Place a bet on each selected line
* 🎰 Generate a random 3×3 slot machine
* 🔤 Four different symbols with different probabilities and payout values
* 🏆 Check winning lines
* 💰 Calculate winnings and total bets
* 📊 Display the current balance
* 🔄 Continue playing with the updated balance
* ❌ Quit the game and display the final balance
* ⚠️ Validate deposits, betting limits, and available balance
* 🖥️ Modern graphical interface using CustomTkinter
* 🌙 Dark-themed interface

## How the Game Works

The slot machine uses four symbols:

| Symbol | Count | Value |
| ------ | ----: | ----: |
| A      |     2 |    $5 |
| B      |     4 |    $4 |
| C      |     6 |    $3 |
| D      |     8 |    $2 |

The number of times a symbol appears in the symbol pool determines its probability of being selected.

For example, `D` appears more frequently than `A`, so `D` has a higher chance of appearing.

### Game Settings

* **Rows:** 3
* **Columns:** 3
* **Maximum betting lines:** 3
* **Minimum bet per line:** $1
* **Maximum bet per line:** $100

## Game Flow

The game follows a simple step-by-step process.

### 1. Deposit

When the application starts, enter the amount you want to use as your starting balance.

```text
What would you like to deposit?

[ Enter amount ]

[ Deposit ]
```

The entered amount becomes your starting balance.

---

### 2. Select Betting Lines

After depositing, choose how many lines you want to bet on.

You can select between:

```text
1 - 3 lines
```

The game validates that the number is within the allowed range.

---

### 3. Enter Your Bet

Enter the amount you want to bet **on each line**.

The allowed bet is:

```text
$1 - $100
```

The game calculates the total bet using:

```text
Total Bet = Bet Per Line × Number of Lines
```

For example:

```text
Bet per line = $10
Lines = 3

Total Bet = $10 × 3
          = $30
```

The game checks whether your current balance is sufficient before allowing the spin.

---

### 4. Spin

After placing a valid bet, press the **SPIN** button.

The game generates a random 3×3 slot machine:

```text
┌─────┬─────┬─────┐
│  A  │  B  │  D  │
├─────┼─────┼─────┤
│  A  │  B  │  C  │
├─────┼─────┼─────┤
│  A  │  B  │  D  │
└─────┴─────┴─────┘
```

---

### 5. Check Winnings

The game checks each selected horizontal line.

For example, if the first line contains:

```text
A | A | A
```

it is a winning line.

The payout is calculated using the symbol's value and the bet:

```text
Winnings = Symbol Value × Bet
```

If `A` has a value of `$5` and the bet is `$10`:

```text
$5 × $10 = $50
```

The winning amount is added to the player's balance.

---

### 6. Play Again

After each spin, the updated balance is displayed.

The **Play Again** button allows the player to start another round without depositing again.

The game returns to the betting-line step:

```text
Current balance: $220

Enter the number of lines to bet on (1-3)
```

The process continues until the player quits or runs out of money.

---

### 7. Quit

Press **Quit** to end the game.

The application displays the remaining balance:

```text
You left with $220
```

## Example Game

A typical game might look like this:

```text
Starting Balance: $100

Lines: 3
Bet per line: $10

Total Bet: $30

A | B | D
A | B | C
A | B | D

Winnings: $150
Winning Lines: 1

Updated Balance: $220
```

The player can then choose **Play Again** or **Quit**.

## Project Structure

```text
Slot-Machine/
│
├── main.py
└── README.md
```

## Requirements

* Python 3.x
* CustomTkinter

The project uses Python's built-in `random` module for generating the slot-machine results.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shweshd/Slot-Machine.git
```

### 2. Open the Project

```bash
cd Slot-Machine
```

### 3. Install CustomTkinter

```bash
pip install customtkinter
```

On some systems:

```bash
pip3 install customtkinter
```

### 4. Run the Application

```bash
python main.py
```

On some systems:

```bash
python3 main.py
```

A graphical slot-machine window will open.

## Main Functions

### `check_winnings()`

Checks the selected betting lines for matching symbols and calculates the winnings.

```python
check_winnings(columns, lines, bet, values)
```

Returns:

* Total winnings
* List of winning lines

---

### `get_slot_machine_spin()`

Generates the random 3×3 slot machine using the available symbols.

```python
get_slot_machine_spin(rows, cols, symbols)
```

Returns the generated slot-machine columns.

---

### `process_step()`

Controls the step-by-step betting process in the GUI.

It handles:

1. Deposit
2. Number of betting lines
3. Bet amount
4. Balance validation
5. Moving the player to the spin stage

---

### `play_spin()`

Generates the slot-machine result, displays it in the GUI, checks winnings, and updates the player's balance.

---

### `play_again()`

Resets the slot display and starts another betting round using the player's current balance.

---

### `quit_game()`

Ends the game and displays the player's remaining balance.

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
* Object-oriented programming
* Python classes
* GUI programming
* Event-driven programming
* CustomTkinter widgets
* Button callbacks
* Managing GUI state
* Basic game logic

## Future Improvements

Possible improvements include:

* 🎰 Add slot-spin animations
* 🔊 Add sound effects
* 🎨 Add custom symbol graphics
* 🏆 Add more winning combinations
* ↘️ Add diagonal winning lines
* 📈 Add betting history
* 💾 Save the player's balance between sessions
* 🪙 Add different coin/balance systems
* 🎯 Add jackpots
* 🏅 Add a high-score system
* ⚙️ Add game settings
* 🌐 Add online leaderboards

## Author

**Shwesh Dubey**

This project was created as part of my Python learning and practice projects.

---

### Built With

**Python** • **CustomTkinter** • **Random Module**

---
