'''
Generate Card
1/30/2023
Python I

Instructions:
Trace the program to determine how it executes and what
it displays. Check your work by running the program.
Finally, let's discuss the following questions...
1. Does the count_down() function return a value?
   How can you tell?
2. Does the get_card() function return a value?
   How can you tell?
3. How does the get_card() function work? 
'''

import random, time


def count_down(start_time):
    '''
    Counts down from the starting number with a 1 second delay
    between each count.
    '''
    for i in range(start_time, 0, -1):
        print(i)
        time.sleep(1)


def get_card():
    '''
    Returns a card with a suit and face value.
    '''
    suit = random.randint(1, 4)
    face = random.randint(1, 13)
    card = ""

    # Adds face value to card
    if face == 11:
        card += "Jack"
    elif face == 12:
        card += "Queen"
    elif face == 13:
        card += "King"
    else:
        card += str(face)

    # Adds suit to card
    if suit == 1:
        card += " of Diamonds"
    elif suit == 2:
        card += " of Hearts"
    elif suit == 3:
        card += " of Clubs"
    else:
        card += " of Spades"

    return card


print("Pick a card!")
count_down(3)
print("Is this your card: " + get_card())
