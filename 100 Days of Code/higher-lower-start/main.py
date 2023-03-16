import random
from art import logo, vs
from game_data import data

def generate(order, m):
  name = data[m]["name"]
  foco = data[m]["follower_count"]
  desc = data[m]["description"]
  ctry = data[m]["country"]
  print(f"Compare {order}: {name}, a {desc}, from {ctry}")
  return foco, m

def guess_validate(a, b, c, e, f):
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  if guess == "A":
    if a > b:
      c += 1
      print(f"Your score: {c}")
      e = False
      f = False
    elif a == b:
      print("Ooops, let's go again!")
      e = False
      f = True
    else:
      print(f"Sorry, that's wrong. Final score: {c}")
      e = True
      f = True
  elif guess == "B":
    if b > a:
      c += 1
      print(f"Your score: {c}")
      e = False
      f = False
    elif b == a:
      print("Ooops, let's go again!")
      e = False
      f = True
    else:
      print(f"Sorry, that's wrong. Final score: {c}")
      e = True
      f = True
  return e, f, c


def main():
  count = 0
  x = 0
  y = 0
  end_game = False
  first_round = True
  while not end_game:
    print(logo)
    n = random.randint(0, len(data))
    if not first_round:
      n = x
      A, x = generate("A", n)
    else:
      A, x = generate("A", n)
    print(vs)
    B, y = generate("B", random.randint(0, len(data)))
    if B > A:
      x = y
    end_game, first_round, count = guess_validate(A, B, count, end_game, first_round)

main()