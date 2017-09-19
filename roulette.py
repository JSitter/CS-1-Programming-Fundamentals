'''Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which '''

import random
random.seed(1)
bank_account = 1000
bet_amount = 0
bet_color = None
bet_number = None

random.seed()
roll = random.randint(0, 37)

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

le_wheel = [{"green": 0}, {"red":1}, {"black":2}, {"red":3}, {"black": 4}, {"red", 5}, {"black", 6}, {"red", 7}, {"black", 8}, {"red":9}, {"black":10}, {"black":11}, {"red":12},
{"black":13}, {"red":14}, {"black":15}, {"red":16}, {"black":17}, {"red":18}, {"red":19}, {"black":20}, {"red":21}, {"black":22}, {"red":23}, {"black":24}, {"red":25}, {"black":26},
{"red", 27}, {"black":28}, {"black":29}, {"red":30}, {"black":31}, {"red":32}, {"black":33}, {"red":34}, {"black":35}, {"red":36}, {"green":0}]
print(le_wheel[roll])
print(roll)

la_wheelia = ["green","red","black","red","black","red","black","red","black", "red","black","black","red","black","red","black","red","black","red","red","black","red","black","red","black","red","black","red","black","black","red","black","red","black","red","black","red","green"]
print(la_wheelia[roll])
print(roll)

def take_bet(color, number, amount):
    bet_color = color
    bet_number = number
    bet_amount = amount

def spin():
    pass


def check_results():
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled.'''
    pass

def payout():
    '''returns total amount won or lost by user based on results of roll. '''
    pass

def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:

    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """
    pass
