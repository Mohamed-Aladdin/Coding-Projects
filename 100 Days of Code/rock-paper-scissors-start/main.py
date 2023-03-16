rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
def game():
  print("Welcome to our Rock, Paper and Scissors game!")
  picks = [rock, paper, scissors]
  result = ""
  
  while True:
    user = input("Type \"rock\", \"paper\" or \"scissors\" to start the game. ")
    computer = random.choice(picks)
    
    if user == "rock":
      print(f"\nYou've picked:\n{rock}")
      if computer == scissors:
        result = "You've won, congrats."
      elif computer == paper:
        result = "You've lost, better luck next time."
      else:
        result = "It's a draw!"
      
    elif user == "paper":
      print(f"\nYou've picked:\n{paper}")
      if computer == rock:
        result = "You've won, congrats."
      elif computer == scissors:
        result = "You've lost, better luck next time."
      else:
        result = "It's a draw!"
        
    elif user == "scissors":
      print(f"\nYou've picked:\n{scissors}")
      if computer == paper:
        result = "You've won, congrats."
      elif computer == rock:
        result = "You've lost, better luck next time."
      else:
        result = "It's a draw!"
      
    else:
      print("\nPlease pick a valid choice.")
      continue
      
    print(f"Computer have picked:\n{computer}")
    print(result)
    replay = input("Press enter to replay (q to quit).")
    
    if replay == "q":
      break
    else:
      continue

game()