import random
from art import logo, vs
from game_data import data
from replit import clear

def random_choice(choice):
  choice_name = choice["name"]
  choice_description = choice["description"]
  choice_country = choice["country"]
  return choice_name + ", " + choice_description + ", from " + choice_country

def answer_check(player_choice, A, B):
  global score 
  global game_on
  if player_choice == "A" and A > B:
    score += 1
  elif player_choice == "B" and B > A:
    score += 1
  else:
    print(f"You are wrong! Final score: {score}")
    game_on = False

game_on = True
score = 0
choice_B = random.choice(data)

while game_on:
  print(logo)
  choice_A = choice_B
  choice_B = random.choice(data)
  if choice_A == choice_B:
    choice_A = random.choice(data)
  print(f"Compare A: {random_choice(choice_A)}")
  print(vs)
  print(f"Against B: {random_choice(choice_B)}")
  player_choice = input("Who has more followers? Type 'A' or 'B': ")
  A = choice_A["follower_count"]
  B = choice_B["follower_count"]
  clear()
  answer_check(player_choice, A, B)
  print(f"You are right! Total score: {score}")
