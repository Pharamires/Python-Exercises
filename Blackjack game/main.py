import random
from art import logo

def deal_card():
  """Returns random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw!"
  elif computer_score == 0:
    return "Lose...opponent has Blackjack!"
  elif user_score == 0:
    return "WIN!! You got Blackjack!"
  elif user_score > 21:
    return "You went over...You lose!"
  elif computer_score > 21:
    return "Opponent wet over...You WIN!"
  elif user_score > computer_score:
    return "You WIN!"
  else:
    return "You lose..."
    
def play_game():

  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to add another card or type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Yours opponent final hand: {computer_cards}, opponent final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play another Blackjack round? 'y' or 'n': ") == "y":
  play_game()
