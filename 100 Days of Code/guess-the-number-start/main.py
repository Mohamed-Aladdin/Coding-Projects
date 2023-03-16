import random
from art import logo

def generate_number():
  number = random.randrange(1, 101)
  return number

def get_mode():
  while True:
    mode = input("Type in 'e' for easy mode, 'h' for hard mode: ").lower()
    if mode == 'e':
      attempts = 10
      return attempts
    elif mode == 'h':
      attempts = 5
      return attempts
    else:
      print("Please choose a valid mode!")

def get_validate_guess(number, attempts):
  while attempts > 0:
    guess = int(input("Please guess a number between 1 and 100: "))
    if guess > number:
      print("Your guess is too high!")
      attempts -= 1
      print(f"You have {attempts} attempts!")
    elif guess < number:
      print("Your guess is too low!")
      attempts -= 1
      print(f"You have {attempts} attempts!")
    else:
      print(f"Your guess is correct! The number is {number}")
      break

def main():
  end_of_game = False
  while not end_of_game:
    print(logo)
    print("Welcome to 'Guess the Number' game!")
    att = get_mode()
    num = generate_number()
    print(f"You have {att} attempts!")
    get_validate_guess(num, att)
    replay = input("Press enter to play again (q to quit): ").lower()
    if replay == 'q':
      end_of_game = True

main()