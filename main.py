import random
import customtkinter as ctk
from tkinter import messagebox


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


# =========================================================
# SLOT MACHINE LOGIC
# =========================================================

def check_winnings(columns, lines, bet, values):

    winnings = 0
    winnings_lines = []

    for line in range(lines):

        symbol = columns[0][line]

        for column in columns:

            symbol_to_check = column[line]

            if symbol != symbol_to_check:
                break

        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):

    all_symbols = []

    for symbol, symbol_count in symbols.items():

        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    for col in range(cols):

        column = []

        current_symbols = all_symbols[:]

        for _ in range(rows):

            value = random.choice(current_symbols)

            current_symbols.remove(value)

            column.append(value)

        columns.append(column)

    return columns


# =========================================================
# GUI
# =========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SlotMachine(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("🎰 Slot Machine")

        self.geometry("600x700")

        self.resizable(False, False)

        # -----------------------------
        # GAME VARIABLES
        # -----------------------------

        self.balance = 0

        self.lines = 0

        self.bet = 0

        self.total_bet = 0

        self.winnings = 0

        self.winnings_lines = []

        # -----------------------------
        # TITLE
        # -----------------------------

        self.title_label = ctk.CTkLabel(
            self,
            text="🎰 SLOT MACHINE",
            font=("Arial", 32, "bold")
        )

        self.title_label.pack(pady=(30, 10))


        # -----------------------------
        # BALANCE
        # -----------------------------

        self.balance_label = ctk.CTkLabel(
            self,
            text="Balance: $0",
            font=("Arial", 22, "bold")
        )

        self.balance_label.pack(pady=10)


        # -----------------------------
        # MAIN CONTENT FRAME
        # -----------------------------

        self.content_frame = ctk.CTkFrame(self)

        self.content_frame.pack(
            padx=30,
            pady=20,
            fill="both",
            expand=True
        )


        # -----------------------------
        # STATUS
        # -----------------------------

        self.status_label = ctk.CTkLabel(
            self.content_frame,
            text="What would you like to deposit?",
            font=("Arial", 18, "bold")
        )

        self.status_label.pack(pady=(25, 15))


        # -----------------------------
        # INPUT
        # -----------------------------

        self.input_entry = ctk.CTkEntry(
            self.content_frame,
            width=300,
            height=40,
            placeholder_text="Enter amount"
        )

        self.input_entry.pack(pady=10)


        # -----------------------------
        # ACTION BUTTON
        # -----------------------------

        self.action_button = ctk.CTkButton(
            self.content_frame,
            text="Deposit",
            width=200,
            height=45,
            font=("Arial", 17, "bold"),
            command=self.process_step
        )

        self.action_button.pack(pady=20)


        # -----------------------------
        # SLOT DISPLAY
        # -----------------------------

        self.slot_frame = ctk.CTkFrame(
            self.content_frame
        )


        self.slot_labels = []


        for row in range(ROWS):

            row_labels = []

            for col in range(COLS):

                label = ctk.CTkLabel(
                    self.slot_frame,
                    text="?",
                    width=90,
                    height=70,
                    font=("Arial", 32, "bold"),
                    fg_color=("gray85", "gray20"),
                    corner_radius=10
                )

                label.grid(
                    row=row,
                    column=col,
                    padx=6,
                    pady=6
                )

                row_labels.append(label)

            self.slot_labels.append(row_labels)


        # -----------------------------
        # RESULT
        # -----------------------------

        self.result_label = ctk.CTkLabel(
            self.content_frame,
            text="",
            font=("Arial", 17),
            wraplength=450
        )

        self.result_label.pack(pady=15)


        # -----------------------------
        # QUIT BUTTON
        # -----------------------------

        self.quit_button = ctk.CTkButton(
            self,
            text="Quit",
            width=150,
            command=self.quit_game
        )

        self.quit_button.pack(pady=20)


        # -----------------------------
        # CURRENT STEP
        # -----------------------------

        self.step = "deposit"


    # =====================================================
    # PROCESS CURRENT STEP
    # =====================================================

    def process_step(self):

        value = self.input_entry.get().strip()


        # =================================================
        # STEP 1 - DEPOSIT
        # =================================================

        if self.step == "deposit":

            if not value.isdigit():

                messagebox.showerror(
                    "Invalid Input",
                    "Please enter a number."
                )

                return


            amount = int(value)


            if amount <= 0:

                messagebox.showerror(
                    "Invalid Amount",
                    "Amount must be greater than 0."
                )

                return


            self.balance = amount


            self.balance_label.configure(
                text=f"Balance: ${self.balance}"
            )


            # Move to next step

            self.step = "lines"


            self.status_label.configure(
                text=f"Balance: ${self.balance}\n\n"
                     f"Enter the number of lines to bet on (1-{MAX_LINES})"
            )


            self.input_entry.delete(0, "end")

            self.input_entry.configure(
                placeholder_text="1 - 3"
            )


            self.action_button.configure(
                text="Continue"
            )


        # =================================================
        # STEP 2 - NUMBER OF LINES
        # =================================================

        elif self.step == "lines":

            if not value.isdigit():

                messagebox.showerror(
                    "Invalid Input",
                    "Please enter a number."
                )

                return


            lines = int(value)


            if not 1 <= lines <= MAX_LINES:

                messagebox.showerror(
                    "Invalid Lines",
                    f"Enter a valid number of lines (1-{MAX_LINES})."
                )

                return


            self.lines = lines


            # Move to next step

            self.step = "bet"


            self.status_label.configure(
                text=f"You selected {self.lines} line(s).\n\n"
                     f"What would you like to bet on each line?"
            )


            self.input_entry.delete(0, "end")

            self.input_entry.configure(
                placeholder_text=f"${MIN_BET} - ${MAX_BET}"
            )


            self.action_button.configure(
                text="Place Bet"
            )


        # =================================================
        # STEP 3 - BET
        # =================================================

        elif self.step == "bet":

            if not value.isdigit():

                messagebox.showerror(
                    "Invalid Input",
                    "Please enter a number."
                )

                return


            bet = int(value)


            if not MIN_BET <= bet <= MAX_BET:

                messagebox.showerror(
                    "Invalid Bet",
                    f"Bet must be between "
                    f"${MIN_BET} and ${MAX_BET}."
                )

                return


            self.bet = bet


            self.total_bet = self.bet * self.lines


            # =================================================
            # CHECK BALANCE
            # =================================================

            if self.total_bet > self.balance:

                messagebox.showwarning(
                    "Insufficient Balance",
                    f"You do not have enough to bet "
                    f"${self.total_bet}.\n\n"
                    f"Current balance: ${self.balance}"
                )

                return


            # =================================================
            # SHOW BET
            # =================================================

            self.status_label.configure(
                text=f"You are betting ${self.bet} "
                     f"on {self.lines} line(s).\n\n"
                     f"Total bet: ${self.total_bet}"
            )


            # Remove bet from balance

            self.balance -= self.total_bet


            self.balance_label.configure(
                text=f"Balance: ${self.balance}"
            )


            # Disable input

            self.input_entry.delete(0, "end")

            self.input_entry.configure(
                state="disabled"
            )


            self.action_button.configure(
                text="SPIN",
                command=self.play_spin
            )


            self.step = "spin"


        # =================================================
        # STEP 4 - SPIN
        # =================================================

        elif self.step == "spin":

            self.play_spin()


    # =====================================================
    # SPIN
    # =====================================================

    def play_spin(self):

        # Generate slot machine

        slots = get_slot_machine_spin(
            ROWS,
            COLS,
            symbol_count
        )


        # Display slots

        for row in range(ROWS):

            for col in range(COLS):

                self.slot_labels[row][col].configure(
                    text=slots[col][row]
                )


        # Show slot frame

        self.slot_frame.pack(
            pady=20
        )


        # Check winnings

        self.winnings, self.winnings_lines = check_winnings(
            slots,
            self.lines,
            self.bet,
            symbol_value
        )


        # Add winnings

        self.balance += self.winnings


        # Update balance

        self.balance_label.configure(
            text=f"Balance: ${self.balance}"
        )


        # =================================================
        # RESULT
        # =================================================

        if self.winnings > 0:

            self.result_label.configure(
                text=f"🎉 You won ${self.winnings}!\n\n"
                     f"Winning lines: "
                     f"{', '.join(map(str, self.winnings_lines))}"
            )

        else:

            self.result_label.configure(
                text=f"You won $0.\n\n"
                     f"No winning lines."
            )


        # =================================================
        # NEXT ROUND
        # =================================================

        self.action_button.configure(
            text="Play Again",
            command=self.play_again
        )


        self.step = "finished"


    # =====================================================
    # PLAY AGAIN
    # =====================================================

    def play_again(self):

        # Check if player has money

        if self.balance <= 0:

            messagebox.showinfo(
                "Game Over",
                "You have no money left."
            )

            self.quit_game()

            return


        # Clear slots

        for row in range(ROWS):

            for col in range(COLS):

                self.slot_labels[row][col].configure(
                    text="?"
                )


        # Clear result

        self.result_label.configure(
            text=""
        )


        # Hide slot machine

        self.slot_frame.pack_forget()


        # Enable input

        self.input_entry.configure(
            state="normal"
        )


        self.input_entry.delete(0, "end")


        # Go back to lines

        self.step = "lines"


        self.status_label.configure(
            text=f"Current balance: ${self.balance}\n\n"
                 f"Enter the number of lines to bet on (1-{MAX_LINES})"
        )


        self.input_entry.configure(
            placeholder_text="1 - 3"
        )


        self.action_button.configure(
            text="Continue",
            command=self.process_step
        )


    # =====================================================
    # QUIT
    # =====================================================

    def quit_game(self):

        messagebox.showinfo(
            "Game Over",
            f"You left with ${self.balance}"
        )

        self.destroy()


# =========================================================
# START PROGRAM
# =========================================================

if __name__ == "__main__":

    app = SlotMachine()

    app.mainloop()