"""This program does stuff. I'll fill this in later. I already wrote the other assignment about what I'm going to do"""
from random import randint

def round ():
    low=0 #Just making low and high in case I want to change it later
    high=100
    a=randint(low,high) #Our random num for the round

    botLow=low
    botHigh=high

    botGuess=randint(botLow,botHigh)

    guess=high+1 #This is so it is always outside of the range

    while guess != a:
        validGuess = False
        while validGuess != True: #Make them keep trying until they get it right
            guess=input("Enter your next guess")
            if guess.isdigit(): #Weeding out nonnumerical inputs and negative numbers so no errors occur
                if int(guess)==round(int(guess)): #Weeding out decimal points so nothing weird happens
                    validGuess=True
                else:
                    print("Your guess must be an integer")
            else:
                print("Your guess must be a number")
