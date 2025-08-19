import random

print("Number guessing game")

# Generate a random number between 1 and 9
number = random.randint(1, 9)

# Initialize chances counter
chances = 1

print("Guess a number (between 1 and 9):")

# While loop for the guessing game
while True:
    # Get user's guess
    guess = int(input())
    
    # Check if guess is correct
    if guess == number:
        print(f'CONGRATULATIONS! YOU HAVE GUESSED THE NUMBER {number} IN {chances} ATTEMPTS!')
        break
    
    # Check if guess is too low
    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)
    
    # Otherwise, guess is too high
    else:
        print("Your guess was too high: Guess a number lower than", guess)
    
    # Increase the chance counter
    chances += 1
