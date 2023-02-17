import random
import time 

def delay():
    delay = time.sleep(1)

name = input("Please type in your name: ").capitalize()
print(f"Welcome {name} to my quiz")
print()

delay()

playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()
else:
    pass

delay()
print()

while playing == "yes":
    
    print("Question 1:")
    options = ["A", "B", "C", "D"]
    score = 0
    answer = input("What is the seventh book of the Bible? ").capitalize()
    correct_answer = "Judges"
    if answer == "Judges":
        print("Correct")
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer} ")

    delay()
    print()

    print("Question 2:")
    print("What is the highest wasterfall in the world?")
    print("'A' = 'Angel Falls', 'B' = 'Victoria Falls', 'C' = 'Niagra Falls', 'D' = 'Tugela Falls' ")
    answer = input(f"Please choose between {options} : ").upper()
    correct_answer = "C"
    if answer == "C":
        print("Correct")
        score += 1
        score
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 3')
    answer = input('What is the name of the volvanco that erupted and destroyed the town of Pompeii in AD 79? ')
    correct_answer = "Mount Vesuvius"
    if answer == correct_answer:
        print("Correct")
        score += 1
    else:
        print(f"Incorrect! The correct asnwer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 4')
    print("What year did the Great Fire of London occur?")
    print("'A' = 1666, 'B' = 1743, 'C' = 1621, 'D' = 1201 'E' = 1665")
    answer = input(f"Please choose between {options} :  ").upper()
    correct_answer = 'A'
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 5')
    random_float = random.uniform(10.5, 50.5)
    print(f"What is {random_float} rounded up to the nearest whole number? ")
    answer = int(input())
    correct_answer = round(random_float)
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 6')
    answer = input("What is the world's largest rainforest? ")
    correct_answer = "The Amazon"
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 7')
    answer = input("'Hey Ya!' was a massive hit for which two man group from Atlanta, USA? ").capitalize()
    correct_answer = 'Outkast'
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 8')
    answer = input("What football club is nickname 'The Eagles' ? ").title()
    correct_answer = 'Crystal Palace'
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 9')
    answer = input("What is the capital of Nigeria? ").capitalize()
    correct_answer = 'Abuja'
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 10 ')
    answer = input(("What TV programme spawned the character Tinky Winky? ")).capitalize()
    correct_answer = 'Teletubbies'
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 11')
    print("What currency is the main tender in Phillipines?")
    print("'A' = 'Rupee, 'B' = 'Peso', 'C' = 'Lira', 'D' = 'Ruble' ")
    answer = input(f"Please choose between {options} :  ").upper()
    correct_answer = 'B'
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 12 ')
    answer = input(("What is the highest grossing film (as of 2023) ? ")).capitalize()
    correct_answer = 'Avatar'
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 13 ')
    answer = input(("Who was the Egyptian god of green things and life, and husband of Isis? ")).capitalize()
    correct_answer = 'Osiris'
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 14')
    print("In which anime is Ash Ketchum the main character?")
    print("'A' = 'Eyeshield 21', 'B' = 'Pokemon', 'C' = 'Cowboy Depop', 'D' = 'Naruto' ")
    answer = input(f"Please choose between {options}:  ").upper()
    correct_answer = 'B'
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Question 15 ')
    answer = input(("Who made the recent album called 'Justice' (2021) ? ")).title()
    correct_answer = 'Justin Bieber'
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('Bonus Question: ')
    answer = input(("Finish the quote: 'You cannot say Pop and forget the ")).capitalize()
    correct_answer = 'Smoke'
    if answer == correct_answer:
        print('Correct')
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer} not {answer}")
    delay()
    print()

    print('End of quiz')
    time.sleep(2)
    print("Calculating score....")
    delay()
    print(f"Your score is {score} ")
    percentage = (score* 100/16)
    print(f"You achieved {percentage} % ")
    print()
    play_again = input("Do you want to play again? ").lower()
    if play_again == "yes":
        print()
        pass
    else:
        exit()
    
