import random
from hangman_words import word_list
from hangman_art import stages, logo

# def welcome():
#   print(logo)
#   play = input("Welcome to the infamous hangman game. Press any key to start (q to quit): ")
#   if play == "q":
#     break
#   else:
#     hash = ""
#     hashing = []
#     word = random.choice(word_list)
#     for _ in range(0, len(word)):
#       hash += "-"
#       hashing.append("-")
#     print(hash)
    

# def replay():
#   user = input("Press any key to play again (q to quit):" )
#   if user == "q":
#     break
#   else:
#     continue

# def user_trials():
#   guess = input("Please guess a letter: ")
#   lives = 7
#   for i in range(0, len(word)):
#     if guess == word[i]:
#       hashing[i] = guess
#       print(f"You've guessed letter {guess} correctly")
#       print(stages[lives])
#       if 
#     else:
#       print("You've guessed wrong.")
#       print(stages[lives-1])

#First: a welcome message with the game's logo asking the user if they want to play or quit.
#Second: word random choice and displaying the hashs.
#Third: prompting the user to guess a letter and checking whether they guessed right or not, displaying the result alongside the stage they're at.
#Fourth: checking if they guessed the whole word yet or not.
#Fifth: prompting the user either to play again or quit.
def main():
  while True:
    print(logo)
    play = input("Welcome to the infamous hangman game. Press enter to start (q to quit): ")
    if play == "q":
      exit()
    else:
      hash = ""
      hashing = []
      word = random.choice(word_list)
      for _ in range(0, len(word)):
        hash += "-"
        hashing.append("-")
      print(hash)

    lives = 6

    while lives > 0:
      count = 0
      guess = input("Please guess a letter: ")
      if hashing.count(guess) > 0:
        print(f"You've guessed letter [{guess}] already!")
        print(stages[lives])
        for j in hashing:
          print(j, end="")
        print("\n")
        continue
      for i in range(0, len(word)):
        if guess == word[i]:
          hashing[i] = guess
          count += 1

      if count > 0:
        print(f"You've guessed letter [{guess}] correctly.")
        print(stages[lives])
        for j in hashing:
          print(j, end="")
        print("\n")
        if hashing.count("-") == 0:
          print("Congrats, you've won! Well played.")
          break

      else:
        lives -= 1
        print("You've guessed wrong.")
        print(stages[lives])
        for j in hashing:
          print(j, end="")
        print("\n")
        if lives == 0:
          print("You've lost the game, better luck next time.")
          break

    user = input("Press enter to play again (q to quit):" )
    if user == "q":
      break
    else:
      continue

main()