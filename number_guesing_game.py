import random

num_lives = 3
guessed_numbers = []

num = random.randint(0, 10)
print(num)
print()
while num_lives != 0:
    guess = int(input(f"Guess the number between {0} and {10}: "))
    while guess < 0 or guess > 10:
        print("Please enter a value between the specified range")
        guess = int(input(f"Guess the number between {0} and {10}: "))
        num_lives = num_lives
    if guess in guessed_numbers:
        guessed_numbers.sort()
        print(f"Please choosed a different number that is not in {guessed_numbers}")
        num_lives = num_lives
    elif guess >= 0 and guess != num and guess not in guessed_numbers:
        num_lives -= 1
        guessed_numbers.append(guess)
        print(f"{guess} is not the correct number")
    elif guess == num:
        print(f"Congratulations.. you won! You guessed the correct number with {num_lives} lives left")
        break
    if num_lives == 0:
        print(f"Game over! You have {num_lives} lives left. The correct number was {num}")
        break
    else:
        pass
print()
print('Thank you for playing')
    
 
