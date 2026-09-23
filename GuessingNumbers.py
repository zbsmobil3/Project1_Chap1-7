"""This program does stuff. I'll fill this in later. I already wrote the other assignment about what I'm going to do"""
from random import randint

#Declaring Initial Vars/Lists
scores=[]
roundsPlayed=0


def validation(isFirstTime): #Created to not go more than 3 deep
    """Makes sure a valid positive interger is entered, and repeats if not."""
    
    validGuess = False
    while validGuess != True: #Make them keep trying until they get it right
                if isFirstTime:
                     guess=input("Enter your first guess ").strip()         
                else:
                     guess=input("Enter your next guess ").strip()                 
                if guess.isdigit(): #Weeding out nonnumerical inputs and negative numbers so no errors occur. Also return false with a decimal point
                    validGuess=True
                else:
                    print("Your guess must be a number")
    return int(guess)


def round ():
    """The Core Loop, run each Round"""

    numGuesses=0
    low=0 #Just making low and high in case I want to change it later
    high=100
    a=randint(low,high) #Our random num for the round

    botLow=low
    botHigh=high

  

    guess=high+1 #This is so it is always outside of the range
    output=""

    while guess != a: #This isn't really needed since I'm using a break instead.
        botGuess=randint(botLow,botHigh)
        if (botLow == low) & (botHigh == high): #Seeing if it is the first time in the round
            guess = validation(True)
        else:
            guess = validation(False)
        numGuesses +=1
        if guess > a:
            output="high"
        elif guess < a:
            output="low"
        else:
            output="right on!"
            break
        if botGuess > a:
             botHigh=botGuess-1
             botOutput="high"
        elif botGuess < a:
            botLow=botGuess+1
            botOutput="low"
        else:
            break
        print(f"You guessed {output}")
        print(f"the bot guessed {botOutput}") #Maybe add later functionality for hiding/showing the bot's guess?
    if guess == a:
         print("Congrats! You won the round! :D")
    else:
         print("The bot won :S")

    #Highscore logic will probably go here
    global roundsPlayed
    roundsPlayed += 1
    global scores
    scores.append(numGuesses)

    print(f"You have played {roundsPlayed} rounds and have gotten the following scores:\n676767")

    newRound=input("Do you want to play again? (y/n)")
    if newRound=="y":
         round()

#Main Body of Code
round()   
        
