# Copyright 2022 PI515

import random

playAgain = True

while playAgain:
  keepAsking = True
  while keepAsking:
    num = input("Type a number for an upper bound: ")
    if num.isdigit():
      print("Let's play!")
      num = int(num)
      keepAsking = False
    else:
      print("Invalid input. Try again.")

  secret = random.randint(1, num)
  guess = None
  count = 0

  while guess != secret:
    guess = input("Type a number between 1 and " + str(num) + ": ")
    if guess.isdigit():
      guess = int(guess)
      if guess == secret:
        print("You got it")
        count = count + 1
      else:
        print("Try again.")
        count = count + 1

  if count == 1:
    print("It took you", count, "guess!")
  else:
    print("It took you", count, "guesses!")

  playAgainInput = input("Do you want to play again? y/n: ")

  if playAgainInput == 'n':
    playAgain = False
