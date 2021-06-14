import random
import replit
from game_data import data
from art import vs 
from art import logo

#select the two data - assign to variables
print(logo)
option_a = random.choice(data)
option_b = random.choice(data)

if option_a == option_b:
  option_b = random.choice(data)

#check two follower counts
def highest_following():
  """Returns which option has the bigger follower count"""
  if option_a["follower_count"] > option_b["follower_count"]:
    return 'A'
  elif option_b["follower_count"] > option_a["follower_count"]:
    return 'B'

game_over = False
user_score = 0

while not game_over:
  #check which data has the highest_following through function
  highest_following()
  #print two data sets
  print("Compare A: " + option_a["name"] + ", a " + option_a["description"] + ", from " + option_a["country"])
  print(vs)
  print("Against B: " + option_b["name"] + ", a " + option_b["description"] + ", from " + option_b["country"])
  #ask for user input
  user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  #compare user input with highest_following
  if user_guess != highest_following():
    game_over = True
    replit.clear()
    print(f"Game over! Your final score is: {user_score}.")
  else:
    user_score += 1
    replit.clear()
    print(f"Your score is: {user_score}")
    if highest_following() == 'A':
      option_b = random.choice(data)
    elif highest_following() == 'B':
      option_a = option_b
      option_b = random.choice(data)
    else:
      print("ERROR IN SYSTEM.")