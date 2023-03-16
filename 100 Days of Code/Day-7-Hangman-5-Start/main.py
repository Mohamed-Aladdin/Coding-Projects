import random
from hangman_words import word_list
from hangman_art import stages, logo

def welcome():
  print(logo)
  play = input("Welcome to the infamous hangman game. Press enter to start (q to quit): ")
  if play == "q":
    exit()

def get_hash():
  lives = 6
  hash = ""
  hashing = []
  word = random.choice(word_list).lower()
  for _ in range(0, len(word)):
    hash += "-"
    hashing.append("-")
  print(hash)
  return word, hashing, lives

def get_guess(word, hashing, guess):
  count = 0
  for i in range(0, len(word)):
    if guess == word[i]:
      hashing[i] = guess
      count += 1
  return count, guess

def user_validation():
  word, hashing, lives = get_hash()

  while lives > 0:
    guess = input("Please guess a letter: ")
    if hashing.count(guess) > 0:
      print(f"You've guessed letter [{guess}] already!")
      print(stages[lives])
      for j in hashing:
        print(j, end="")
      print("\n")
      continue

    count, guess = get_guess(word, hashing, guess)

    if count > 0:
      print(f"You've guessed letter [{guess}] correctly.")
      print(stages[lives])
      for j in hashing:
        print(j, end="")
      print("\n")
      if hashing.count("-") == 0:
        print(f"Congrats, you've won! The word is {word}.")
        break
      
    else:
      lives -= 1
      print("You've guessed wrong.")
      print(stages[lives])
      for j in hashing:
        print(j, end="")
      print("\n")
      if lives == 0:
        print(f"You've lost the game. The word is {word}.")
        break

def main():
  welcome()
  while True:
    user_validation()
    user = input("Press enter to play again (q to quit):" )
    if user == "q":
      break
    else:
      continue

main()