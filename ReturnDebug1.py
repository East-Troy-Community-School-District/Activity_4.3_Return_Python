'''
Return Debug 1
1/30/2023
Python I

Instructions:
Run the program several times. You should notice that the program
always prints "Outlook good." Obviously, this is not the intention
of the function. There is something wrong with the function.
Fix the function so that each message has a chance to be displayed.
How many returns can a function have?
'''

import random


def message(num):
    '''
    Returns a message.
    '''
    return "Outlook good."
    if num == 1:
        return "It is certain."
    elif num == 2:
        return "Yes."
    elif num == 3:
        return "Cannot predict now."


print(message(random.randint(1, 20)))
