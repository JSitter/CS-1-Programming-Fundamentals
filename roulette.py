'''Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which '''

import random

bank_account = 1000
bet = 0




green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

#print("\nAllowed Bets:\nEven, Odd, Low (Numbers 1 to 18), High (Number 19 to 36), \nFirst Twelve, Second Twelve, Third Twelve, \n First Column, Second Column, Third Column\n Red, Black, or any specific number\n")


le_wheel = ["green","red","black","red","black","red","black","red","black","red","black","black","red","black","red","black","red","black","red","red","black","red","black","red","black","red","black","red","black","black","red","black","red","black","red","black","red","green"]

bet_space = None
def take_bet(space, bet_amount):
    print("bet: " + space)
    bet_space = space
    bet = bet_amount
    print("space bet: " + bet_space)
    

def spin():
    random.seed()
    return random.randint(0, 37)


def check_results():
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled.'''
    print(bet_space)
    if(bet_space == "Even"):
        if(spin() % 2 == 0):
            print("you won")
        else:
            print("Loser!")
        


def payout(leverage):
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
    

    spc_bet = input("Bet on a space: ")
    bet_amt = input("Place your bet amount: ")
    print(spc_bet)
    take_bet(spc_bet, bet_amt)
    check_results()
    


play_game()