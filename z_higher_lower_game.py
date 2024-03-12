import random
import time

class higher_lower:

    def __init__(self):
        self.highest_score = 0
        self.score = 0
        self.alive = True
        self.random_number = random.randint(1, 11)
    
    def delay(self):
        time.sleep(1)

    def get_initial_high_score(self):
        self.highest_score = 0

    def check_if_player_is_alive(self):
        if self.alive:
            self.score = 0
            self.alive = True
        return self.alive

    def play_game(self):
        while self.alive:
            print(self.random_number)
            self.user_guess = input("Is the next number higher or lower? ").title()
            while self.user_guess not in ['Higher', 'Lower']:
                print("Please enter either 'lower' or 'higher'")
                self.user_guess = input("Is the next number higher or lower? ").title()
            self.new_number = random.randint(1, 11)
            if self.new_number < self.random_number and self.user_guess == 'Lower':
                print(f"{self.user_guess}. You are correct")
                self.score += 1
                self.random_number = self.new_number
            elif self.new_number > self.random_number and self.user_guess == 'Higher':
                print(f"{self.user_guess}. You are correct")
                self.score += 1
                self.random_number = self.new_number
            else:
                print(f"{self.user_guess}. Unlucky")
                self.alive = False
                break
        print(f"Your score for this round is: {self.score}")
        
    def getting_high_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            print(f"New highest score: {self.highest_score}")

    def play_another_round(self):
        while True:
            self.play_again = input("Do you want to play again? (yes/no): ").lower()
            while self.play_again not in ['yes', 'no']:
                print("Please enter either 'yes' or 'no'")
                self.play_again = input("Do you want to play again? (yes/no): ").lower()
            if self.play_again == 'yes':
                self.random_number = random.randint(1, 11)
                self.alive = True
                return True
            elif self.play_again == 'no':
                print()
                print('Thank you for playing :) ')
                print()
                self.delay()
                print(f"Your highest score overall is: {self.highest_score}")
                self.alive = False
                return False
            else:
                print("Please type either 'yes' or 'no' ")
    
game = higher_lower()
while game.check_if_player_is_alive():
    game.play_game()
    game.getting_high_score()
    go_again = game.play_another_round()
    if go_again is not True:
        break




