import random
import time

random_guess = random.random()
if random_guess >= 0.5:
  random_guess = "heads"
else:
  random_guess = "tails"
random_guess_1 = random.randint(0,10)
if random_guess_1 >= 5:
  random_guess_1 = "heads"
else:
  random_guess_1 = "tails"
  
def random_choice():
  guess = input("Please enter your guess (Heads or Tails): ").lower()
  while guess != "heads" and guess != "tails":
    print("Sorry, Invalid Choice")
    guess = input("Please enter (Heads or Tails): ").lower()
  else:
    if random_guess == guess:
      print("Congratulations! You Won!\nThe computer's coin toss result was: " + random_guess.capitalize())
    else:
      print("Sorry, You Lost!\nThe computer's coin toss result was: " + random_guess.capitalize())


def randint_choice():
  guess = input("Please enter your guess (Heads or Tails): ").lower()
  while guess != "heads" and guess != "tails":
    print("Sorry, Invalid Choice")
    guess = input("Please enter (Heads or Tails): ").lower()
  else:
    if random_guess_1 == guess:
      print("Congratulations! You Won!\nThe computer's coin toss result was: " + random_guess.capitalize())
    else:
      print("Sorry, You Lost!\nThe computer's coin toss result was: " + random_guess.capitalize())




#code
print("Welcome to the Coin Guessing Game!")
time.sleep(1)
print(""" 
Choose a method to toss the coin:
1. Using random.random()
2. Using random.randint()
""")
choice = input("Enter your choice (1 or 2): ")
while choice != "1" and choice != "2":
  print("Sorry, Invalid Choice")
  choice = input("Please enter (1 or 2): ")
if choice == "1":
  random_choice()
elif choice == "2":
  randint_choice()



