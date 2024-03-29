import random

MIN_BET = 1
MAX_BET = 100
MAX_LINES = 3

ROWS = 3
COLS = 3

symbol_count = {
  "A" : 2,
  "B" : 4,
  "C" : 6,
  "D" : 8
  }

symbol_value = {
  "A" : 5,
  "B" : 4,
  "C" : 3,
  "D" : 2
}

def get_slot_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)
  columns = []
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)
    columns.append(column)
  return columns

def print_slot(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], end = " | ")
      else:
        print(column[row], end = "")
    print()

def check_winnings(columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
    else:
      winnings += values[symbol] * bet
      winning_lines.append(line + 1)
  return winnings, winning_lines

def deposit():
  while True:
    amount = input("How much would you like to deposit? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("The amount must be greater than $0.")
    else:
      print("Please enter a valid number.")
  return amount

def get_bet():
  while True:
    amount = input("How much would you like to bet on each line? $")
    if amount.isdigit():
      amount = int(amount)
      if MIN_BET <= amount <= MAX_BET:
        break
      else:
        print(f"The amount must be between ${MIN_BET} and ${MAX_BET}.")
    else:
      print("Please enter a valid number.")
  return amount

def get_num_lines():
  while True:
    lines = input(f"Please enter the number of lines to bet on [1 - {MAX_LINES}]? ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print(f"The number of lines must be between [1 and {MAX_LINES}].")
    else:
      print("Please enter a valid number.")
  return lines

def spin(balance):
  lines = get_num_lines()
  while True:
    bet = get_bet()
    total_bet = bet * lines
    if total_bet > balance:
      print(f"You don't have enough money in your balance to bet that amount, your current balance is ${balance}")
    else:
      break
  print(f"You're betting ${bet} on {lines} lines, total bet is equal to: ${total_bet}")

  slots = get_slot_spin(ROWS, COLS, symbol_count)
  print_slot(slots)
  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
  print(f"You won ${winnings}.")
  print(f"You won on lines:", *winning_lines)
  return winnings - total_bet

def main():
  balance = deposit()
  while True:
    print(f"Your current balance is ${balance}.")
    answer = input("Press Enter to play, (q to quit).")
    if answer == "q":
      break
    balance += spin(balance)
  print(f"You've left with ${balance}.")

main()