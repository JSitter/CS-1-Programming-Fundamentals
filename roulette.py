'''Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which '''

import random
import os
import time

#Features for version 2.0
#print("\nAllowed Bets:\nEven, Odd, Low (Numbers 1 to 18), High (Number 19 to 36), \nFirst Twelve, Second Twelve, Third Twelve, \n First Column, Second Column, Third Column\n Red, Black, or any specific number\n")


le_wheel = ["green","red","black","red","black","red","black","red","black","red","black","black","red","black","red","black","red","black","red","red","black","red","black","red","black","red","black","red","black","black","red","black","red","black","red","black","red","green"]
bet_space = None
green = [0, "00"]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
bet = 0
bank_account = 1000

def take_bet(space, bet_amount):
    global bank_account
    global bet
    global bet_space

    bet_space = space
    bank_account = bank_account - int(bet_amount)
    bet = int(bet_amount)
    

def spin():
    random.seed()
    return random.randint(0, 37)


def check_results():
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled.'''
    global le_wheel
    global bet_space
    result = spin()
    print(le_wheel[result] + " " + str(result) + "!")
    if le_wheel[result] == bet_space:
        print("Winning Color!")
        if(le_wheel[result] == "green"):
            print("Green Bonus!")
            payout(7)
        payout(2)

    if result == bet_space:
        print("Winning Number!")
        payout(7)
    
    if (result != bet_space) and (le_wheel[result] != bet_space):
        print("Sorry!")

def payout(leverage):
    '''returns total amount won or lost by user based on results of roll. '''
    global bet
    global bank_account
    winnings = str(bet * leverage - bet)
    print("You won $" + winnings + " *Ding* *Ding* *Ding*")
    bank_account = bank_account + bet * int(leverage)
    print("Your bank account has $" + str(bank_account))


def spinning_animation():
    spin_speed = 0.0
    spinning = True
    spin_times = 7
    spin_index = 0
    spinner = ['|', "/", "-", "\\"]
    os.system('clear')
    print("")
    while spinning:
        for rod in spinner:
            print(rod, end='\r')
            time.sleep(spin_speed)
        spin_index = spin_index + 1
        spin_speed = spin_speed + .1
        if spin_index == spin_times:
            spinning = False

def verify_number(color, number):
    global black, red, green
    if(color == "red"):
        print(number)
        return int(number) in red
    if(color == "black"):
        return int(number) in black
    
    if(color == "green"):
        return int(number) in green

def play_game():
    in_game = True
    valid_number = False
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:

    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """
    while(in_game):
        spc_bet = input("Bet red, black or green: ")
        
        while(not valid_number):
            print("Here are the "+spc_bet+" numbers:")

            if(spc_bet == 'red'):
                for number in red :
                    print(number)

            if(spc_bet == 'black'):
                for number in black :
                    print(number)

            if(spc_bet == 'green'):
                for number in green :
                    print(number) 

            bet_number = input("Which number would you like to bet on?")
            print("You have $" + str(bank_account) + " in your gambling fund.")
            valid_number = verify_number(spc_bet, bet_number)
        
        if(bet_number == "00"):
            bet_number = "37"

        bet_amt = input("Place your bet amount: ")
        take_bet(spc_bet, bet_amt)
        spinning_animation()
        check_results()
        replay = input("Would you like to play again? y or n ")
        if replay == "n":
            in_game = False
        
    


play_game()