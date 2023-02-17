import additional_files
import random

word_lists_by_difficulty_index = {
    'easy': ['cat', 'red', 'dog' ],
    'medium': ['apple', 'chair', 'tiger'],
    'difficult': ['legislate', 'technique', 'parallel']
}

def get_words():
    words = additional_files.choice_of_words
    return words

get_words()

options = ['easy', 'medium', 'difficult']

while True: 
    try:
        difficulty_index = (input(f"Please pick between the options {options}: "))
        if difficulty_index not in options:
            raise ValueError
    except ValueError:
        print("Please enter a valid difficulty ")
        continue
    else:
        break

target_word = random.choice(word_lists_by_difficulty_index[difficulty_index])

letters = list(target_word)
random.shuffle(letters)
shuffled_word = "".join(letters)

print("Here is your shuffled word: " + shuffled_word)

answer = input("What do you think this is an anagram from? ")

print("You answered: " + answer)

if answer == target_word:
    print("Correct!")
else:
    print("That's not correct! The correct answer was " + target_word)