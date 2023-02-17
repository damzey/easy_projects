import time
def delay():
    sleep = time.sleep(1)

name  = input("Type your name: ").capitalize()
print("Welcome", name, "to this adventure ")
print('In this game you will take the role of the protaganist and you are required to make choices that will determine your outcome')

delay()
print()

print('In this scenario, imagine you are going hiking and you fall down a cave, finding yourself in a tunnel')
print()
answer = input("There are two exits to the tunnel, left or right. Type left to go left, and right to go right: ").lower()
if answer == "left":
    delay()
    print()
    print("You successfuly escaped the tunnel with no harm but you are now very hungry")
    answer = input("You now come across a dead starfish and a dead crab. Which one do you eat? Type starfish or crab: ").lower()
    if answer == "starfish":
        delay()
        print()
        print("The starfish was not prepared and cooked very well, and you died from food poisoning")
    elif answer == "crab":
        delay()
        print()
        print("Luckily you knew how to properly cook crabs so you ate the crab and survived")
        print("Now that you have eaten you need to find water to drink ")
        answer = input("You come across a coconut tree. Do you decide to drink the coconut milk or not? Type yes or no: ").lower()
        if answer == 'no':
            delay()
            print()
            print('You pass out from dehydration and do not survive ')
        elif answer == 'yes':
            delay()
            print()
            print('You have now eaten and been replinished. You now need to decide where to find shelter.')
            print('You can either go in two directions, towards the highway or towards the fields')
            answer = input('Do you go towards the highway or fields? Type highway or field: ').lower()
            if answer == 'field':
                print()
                print('You get lost in the fields and eventually you do not get rescued')
            elif answer == 'highway':
                print()
                print('Whilst looking for shelter you meet a mysterious man. But he surprisingly has a radio')
                print('He has already been in contact with rescuers and they are own their way.')
                print('You have been saved! Congratulations :) ')
                delay()
                print()
                print("Side note: Don't talk to strangers!") 

elif answer == "right":
    delay()
    print()
    print('You made it out of the tunnel alive but you ended up breaking your arm.')
    print('After escaping the tunnel, you walk for a mile before getting to a bridge but it looks wobbly')
    answer = input('Should you cross the bridge or go around it? Type cross or walk: ').lower()
    if answer == "walk":
        delay()
        print()
        print('You walked and walked but you could not reach the promised land, and were not rescued')
    elif answer == 'cross':
        delay()
        print()
        print('You took the risk and cross the bridge, but you made it across the bridge safely')
        print('Having found food and water, you are walking and you spot a mysterious person')
        answer = input('Do you talk to the mysterious person or do you avoid him? Type talk or avoid: ')
        if answer == 'avoid':
            delay()
            print()
            print('You avoided the mysterious man but you end up not being rescued')
        elif answer == 'talk':
            delay()
            print()
            print('The mysterious person happens to be a paramedic and offers to take you to a nearby hospital')
            print('You are saved! Congratulations :)')
            delay()
            print()
            print("Side note: Don't talk to strangers!") 
        else:
            exit

print()
print("Thank you for trying", name)
