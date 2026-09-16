# 🎰 Python Slot Machine

A **GUI-based slot machine game built with Python and CustomTkinter**.

This project simulates a simple slot machine where players deposit money, choose betting lines, place bets, spin the machine, and receive winnings based on matching symbols.

It was built as a Python practice project to apply **functions, loops, dictionaries, lists, randomization, input validation, object-oriented programming, and GUI development** in a complete application.

---

## ✨ Features

* 💰 Deposit an initial balance
* 🎯 Choose **1–3 betting lines**
* 💵 Set a bet amount for each line
* 🎰 Generate a random **3×3 slot machine**
* 🔤 Four symbols with different probabilities and payouts
* 🏆 Detect winning lines
* 💰 Calculate winnings automatically
* 📊 Display the current balance
* 🔄 Continue playing without depositing again
* ❌ Quit the game and display the final balance
* ⚠️ Validate deposits, betting limits, and available balance
* 🖥️ Modern GUI built with **CustomTkinter**
* 🌙 Dark-themed interface

---

## 🎮 How It Works

The game follows a simple betting and spinning system.

### 1. Deposit

When the application starts, enter the amount you want to use as your starting balance.

```text
Enter deposit amount

[ 100 ]

[ Deposit ]
```

The deposited amount becomes the player's starting balance.

---

### 2. Choose Betting Lines

After depositing, choose how many horizontal lines you want to bet on.

```text
1 - 3 lines
```

The game validates that the selected number is within the allowed range.

---

### 3. Place Your Bet

Enter the amount you want to bet **on each line**.

```text
Minimum bet: $1
Maximum bet: $100
```

The total bet is calculated using:

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

The game also checks whether the player's balance is sufficient.

---

### 4. Spin the Machine

After entering a valid bet, press the **SPIN** button.

The game generates a random **3×3 slot machine**.

Example:

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

### 5. Calculate Winnings

The game checks the selected horizontal lines for matching symbols.

For example:

```text
A | A | A
```

is a winning line.

Each symbol has a predefined payout value.

```text
Winnings = Symbol Value × Bet Per Line
```

If `A` has a value of `$5` and the bet is `$10`:

```text
$5 × $10 = $50
```

The winnings are added to the player's balance.

---

### 6. Play Another Round

After the spin, the updated balance is displayed.

The **Play Again** option starts another betting round using the remaining balance.

The player does not need to deposit again.

The game continues until the player quits or no longer has enough money to place a bet.

---

### 7. Quit

Press **Quit** to end the game.

The final balance is displayed:

```text
You left with $220
```

---

## 🎰 Game Configuration

| Setting            | Value |
| ------------------ | ----: |
| Rows               |     3 |
| Columns            |     3 |
| Betting Lines      |   1–3 |
| Minimum Bet / Line |    $1 |
| Maximum Bet / Line |  $100 |

### Symbols & Payouts

| Symbol | Frequency | Payout Value |
| :----: | --------: | -----------: |
|    A   |         2 |           $5 |
|    B   |         4 |           $4 |
|    C   |         6 |           $3 |
|    D   |         8 |           $2 |

The frequency of each symbol in the symbol pool determines how often it can be selected.

For example, `D` appears **8 times** while `A` appears only **2 times**, giving `D` a higher probability of appearing.

---

## 📊 Example Game

```text
Starting Balance: $100

Lines: 3
Bet Per Line: $10

Total Bet: $30

A | B | D
A | B | C
A | B | D

Winning Lines: 1
Winnings: $50

Updated Balance: $120
```

The player can then choose to **Play Again** or **Quit**.

---

## 🖥️ Project Structure

```text
Slot-Machine/
│
├── main.py          # Main application
└── README.md        # Project documentation
```

---

## 🛠️ Technologies Used

* **Python 3**
* **CustomTkinter**
* **Random module**

### Python Concepts Used

* Variables and constants
* Lists and dictionaries
* `for` and `while` loops
* Conditional statements
* Functions
* Function parameters and return values
* Input validation
* String formatting
* Nested loops
* List manipulation
* Random selection
* Classes and objects
* Object-oriented programming
* GUI programming
* Event-driven programming
* Button callbacks
* GUI state management

---

## 📦 Requirements

Before running the project, make sure you have:

* Python **3.x**
* CustomTkinter

The `random` module is included with Python and does not require separate installation.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shweshd/Slot-Machine.git
```

### 2. Navigate to the Project

```bash
cd Slot-Machine
```

### 3. Install CustomTkinter

```bash
pip install customtkinter
```

If your system uses `pip3`:

```bash
pip3 install customtkinter
```

### 4. Run the Game

```bash
python main.py
```

Or:

```bash
python3 main.py
```

The slot machine GUI should now open.

---

## 🧩 Main Functions

### `check_winnings()`

Checks the selected betting lines for matching symbols and calculates the player's winnings.

```python
check_winnings(columns, lines, bet, values)
```

**Returns:**

* Total winnings
* Winning lines

---

### `get_slot_machine_spin()`

Generates the random slot-machine result based on the configured rows, columns, and symbols.

```python
get_slot_machine_spin(rows, cols, symbols)
```

**Returns:**

* Generated slot-machine columns

---

### `process_step()`

Controls the betting workflow inside the GUI.

It handles:

1. Deposit
2. Number of betting lines
3. Bet amount
4. Balance validation
5. Moving the player to the spin stage

---

### `play_spin()`

Handles the main spin operation.

It:

1. Generates the slot-machine result
2. Displays the result
3. Checks for winning lines
4. Calculates winnings
5. Updates the player's balance

---

### `play_again()`

Resets the slot display and starts another betting round using the player's current balance.

---

### `quit_game()`

Ends the current game and displays the player's remaining balance.

---

## 🔄 Game Flow

```text
┌───────────────┐
│ Start Game    │
└───────┬───────┘
        ↓
┌───────────────┐
│ Deposit Money │
└───────┬───────┘
        ↓
┌───────────────┐
│ Choose Lines  │
└───────┬───────┘
        ↓
┌───────────────┐
│ Place Bet     │
└───────┬───────┘
        ↓
┌───────────────┐
│ Spin          │
└───────┬───────┘
        ↓
┌───────────────┐
│ Check Results │
└───────┬───────┘
        ↓
┌───────────────┐
│ Update Balance│
└───────┬───────┘
        ↓
   ┌────┴────┐
   ↓         ↓
Play Again   Quit
   │         │
   └──→ Game ┘
```

---

## 💡 What I Learned

This project helped me move from writing small Python programs to building a more complete application with a graphical interface.

Through this project, I practiced:

* Structuring a Python application into reusable functions
* Managing application state
* Working with lists and dictionaries
* Generating randomized results
* Validating user input
* Connecting GUI buttons to Python functions
* Building interfaces with CustomTkinter
* Applying object-oriented programming
* Implementing game logic
* Updating GUI elements dynamically

---

## 🔮 Future Improvements

Planned improvements include:

* 🎰 Add slot-spin animations
* 🔊 Add sound effects
* 🎨 Replace text symbols with custom graphics
* ↘️ Add diagonal winning lines
* 🏆 Add more winning combinations
* 💾 Save player balance between sessions
* 📊 Add betting history
* 🪙 Add different coin/balance systems
* 🎯 Add jackpot mechanics
* 🏅 Add a high-score system
* ⚙️ Add customizable game settings
* 🌐 Add online leaderboards

---

## 👨‍💻 Author

**Shwesh Dubey**

A Python practice project focused on learning **GUI development, programming fundamentals, and application logic**.

---

## 🧰 Built With

**Python** • **CustomTkinter** • **Random Module**

---
