import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}

def clear_screen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

def announce_winner():
  highest_bid = 0
  winner = ""
  for bidder in bids:
    if bids[bidder] > highest_bid:
      highest_bid = bids[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

def get_bid():
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bids[name] = bid
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  clear_screen()
  if more_bidders == "yes":
    get_bid()
  else:
    announce_winner()

get_bid()