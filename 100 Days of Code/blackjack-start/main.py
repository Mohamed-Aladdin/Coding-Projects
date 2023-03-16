import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_init_cards():
  dealer_hand = []
  player_hand = []
  while len(player_hand) < 2 and len(dealer_hand) < 2:
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
  if dealer_hand.count(11) >= 1 and 21 < sum(dealer_hand) < 23:
    dealer_hand.remove(11)
    dealer_hand.append(1)
  elif player_hand.count(11) >= 1 and 21 < sum(player_hand) < 23:
    player_hand.remove(11)
    player_hand.append(1)
  
  return player_hand, dealer_hand

def deal_card(person_hand):
  person_hand.append(random.choice(cards))

def check_winner(player_hand, dealer_hand):
  if dealer_hand.count(11) >= 1 and sum(dealer_hand) > 21:
    dealer_hand.remove(11)
    dealer_hand.append(1)
    print(f"Dealer's hand is: {dealer_hand}")
  elif player_hand.count(11) >= 1 and sum(player_hand) > 21:
    player_hand.remove(11)
    player_hand.append(1)
    print(f"Your hand is: {player_hand}")

  if sum(player_hand) < 22:
    if sum(dealer_hand) > 21 or sum(player_hand) > sum(dealer_hand):
      print("You win!")
    elif sum(dealer_hand) > sum(player_hand):
      print("Dealer wins!")
    else:
      print("It's a draw!")
  elif sum(player_hand) == sum(dealer_hand) or (sum(player_hand) > 21 and sum(dealer_hand) > 21):
    print("It's a draw!")
  else:
    print("You're busted!")

def ask(dummy_hand, player_hand):
  answer = input("Please type in 'h' to hit, 's' to stand: ").lower()
  if answer == "h":
    deal_card(player_hand)
    print(f"Dealer's hand is: {dummy_hand}")
    print(f"Your hand is: {player_hand}")
    return True
  else:
    return False

def main():
  print(logo)
  print("Welcome to the Halal BlackJack house!")
  play = input("Press enter to play (q to quit): ").lower()
  if play == "q":
    exit()
  player_hand, dealer_hand = get_init_cards()
  dummy_hand = []
  while True:
    for _ in range(len(dealer_hand)-1):
      dummy_hand.append(dealer_hand[_])
    print(f"Dealer's hand is: {dummy_hand}")
    print(f"Your hand is: {player_hand}")

    a = True
    b = 0
    while a:
      a = ask(dummy_hand, player_hand)
      if sum(player_hand) >= 21:
        if player_hand.count(11) == 0:
          break
        elif player_hand.count(11) > 0 and b < 1:
          b += 1
          continue
        else:
          break

    if sum(dealer_hand) < 17:
      deal_card(dealer_hand)
    print(f"Dealer hand is: {dealer_hand}")
    print(f"Your hand is: {player_hand}")

    check_winner(player_hand, dealer_hand)

    replay = input("Press enter to play again (q to quit): ").lower()
    if replay == "q":
      break
    else:
      main()

main()


############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

