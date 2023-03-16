import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(msg, cypher):
  new_msg = ""
  for letter in msg:
    if letter not in alphabet and letter != " ":
      print("Please type alphabets only.")
      return False
    elif letter == " ":
      continue
    else:
      index = alphabet.index(letter) + cypher
      if index > len(alphabet) - cypher:
        index = math.fabs(index - len(alphabet) -1) 
      new_letter = alphabet[index]
      new_msg += new_letter
  print(new_msg)

def decrypt(msg, cypher):
  new_msg = ""
  for letter in msg:
    if letter not in alphabet and letter != " ":
      print("Please type alphabets only.")
      return False
    elif letter == " ":
      continue
    else:
      index = alphabet.index(letter) - cypher
      # if index < len(alphabet) + cypher:
      #   index = math.fabs(index - len(alphabet) -1) 
      new_letter = alphabet[index]
      new_msg += new_letter
  print(new_msg)

def main():
  print("Welcome to Caesar Cipher!")
  while True:
    msg = input("Please type in your message: ").lower()
    cypher = int(input("Please specify the shifting parameter: "))
    choice = input("Press 'e' for encryption, 'd' for decryption (q to quit): ").lower()
    if choice == "e":
      encrypt(msg, cypher)
    elif choice == "d":
      decrypt(msg, cypher)
    elif choice == "q":
      print("Thanks for using our tool!")
      break
    else:
      print("Please choose a valid answer!")
    replay = input("Would you like to encrypt/decrypt anything else? Press enter to restart(q to quit)").lower()
    if replay == "q":
      print("Thanks for using our tool!")
      break
    else:
      continue

main()