from art import logo
import random

print(logo)


game_number = random.randint(1, 100)
level = input("Type 'normal' for normal difficulty level; type 'hard' for a more challenging play: ")


def game_on():
  IS_GAME_OFF = False
  if level == "normal":
    number_of_turns = 10
  else:
    number_of_turns = 5
  while IS_GAME_OFF == False:
    player_number = int(input("What is your guessed number?: "))
    number_of_turns -= 1
    if player_number < game_number:
      print("Too low")
      print(f"Number of turns left: {number_of_turns}")
    elif player_number > game_number:
      print("Too high")
      print(f"Number of turns left: {number_of_turns}")
    else:
      IS_GAME_OFF = True
      print(f"{game_number} - yes! this is correct number!")
    if number_of_turns == 0:
      IS_GAME_OFF = True
      print("You run out of turns. Game over...")
      return
      
game_on()