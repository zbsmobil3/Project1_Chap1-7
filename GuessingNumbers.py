"""This program does stuff. I'll fill this in later. I already wrote the other assignment about what I'm going to do"""
from random import randint

def validation(): #Created to not go more than 3 deep
    """Makes sure a valid positive interger is entered, and repeats if not."""
    
    validGuess = False
    while validGuess != True: #Make them keep trying until they get it right
                guess=input("Enter your next guess")
                if guess.isdigit(): #Weeding out nonnumerical inputs and negative numbers so no errors occur. Also return false with a decimal point
                    print("Your guess must be an integer")
                else:
                    print("Your guess must be a number")
    return guess


def round ():
    """The Core Loop, run each Round"""


    low=0 #Just making low and high in case I want to change it later
    high=100
    a=randint(low,high) #Our random num for the round

    botLow=low
    botHigh=high

    botGuess=randint(botLow,botHigh)

    guess=high+1 #This is so it is always outside of the range
    output=""

    while guess != a: #This isn't really needed since I'm using a break instead.
        guess = validation()
        if guess > a:
            output="high"
        elif guess < a:
            output="low"
        else:
            output="right on!"
            break
        
        
