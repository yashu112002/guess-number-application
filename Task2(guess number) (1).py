import random

def play_game():
  """Sets up and plays the guess the number game."""
  # Set difficulty level (easy, medium, hard)
  difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
  
  # Set range based on difficulty
  if difficulty == "easy":
    range_min, range_max = 1, 10
  elif difficulty == "medium":
    range_min, range_max = 1, 25
  else:
    range_min, range_max = 1, 50
  
  # Secret number generation
  secret_number = random.randint(range_min, range_max)
  
  # Set number of guesses based on difficulty
  if difficulty == "easy":
    guesses = 6
  elif difficulty == "medium":
    guesses = 4
  else:
    guesses = 3
  
  # Play the game
  print(f"I'm thinking of a number between {range_min} and {range_max}. You have {guesses} guesses.")
  while guesses > 0:
    try:
      guess = int(input("Take a guess: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue
    
    if guess == secret_number:
      print("Congratulations! You guessed the number!")
      break
    elif guess < secret_number:
      print("Your guess is too low.")
      guesses -= 1
    else:
      print("Your guess is too high.")
      guesses -= 1
    
    if guesses > 0:
      print(f"You have {guesses} guesses left.")
  
  if guesses == 0:
    print(f"Sorry, you ran out of guesses. The number was {secret_number}.")

if __name__ == "__main__":
  play_game()