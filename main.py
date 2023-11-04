import random
MAX_LINES= 3
MAX_BET = 200
MIN_BET = 10

Rows = 3
Cols = 3

symbol_count ={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value ={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winning(colums, Lines, bet, values):
    winning = 0
    winning_line = []
    for line in range(Lines):
        symbol = colums[0][line]
        for column in colums:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol] * bet
            winning_line.append(Lines + 1)

    return winning, winning_line


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols =[]
    for symbols,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbols)

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

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("Deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount

def line_numbers():
    while True:
        Lines = input(f"Enter number of lines from 1 - {str(MAX_LINES)}:  ")
        if Lines.isdigit():
            Lines = int(Lines)
            if 1 <= Lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    return Lines
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET} ")
        else:
            print("Enter Amount: ")
    return amount
def game(balance):
    Lines = line_numbers()
    while True:
        bet = get_bet()
        total_bet = bet * Lines
        if total_bet > balance:
            print("Insufficient funds")
        else:
            break
    print(f"You are betting ${bet} on {Lines} line. Total bet is ${total_bet}")

    slot = get_slot_machine_spin(Rows, Cols, symbol_count)
    print_slot_machine(slot)
    winnings, winning_lines = check_winning(slot, Lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == 'q':
            break
        balance += game(balance)

    print(f"You left with ${balance}")



main()