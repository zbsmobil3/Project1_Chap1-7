from random import *

class Settings():
    
    def __init__(HighLowSelf):
        """A class to set up vars. Were you expecting smth else???"""
        #SETTING UP VARS:
        HighLowSelf.scores=[]
        HighLowSelf.roundsPlayed=0

    def _set_up_every_round_vars(HighLowSelf): #I don't know if I could've made that function name any longer :B
        HighLowSelf.a=randint(HighLowSelf.low,HighLowSelf.high) #Our random num for the round
        HighLowSelf.numGuesses=0
        HighLowSelf.botLow=HighLowSelf.low
        HighLowSelf.botHigh=HighLowSelf.high
        HighLowSelf.guess=HighLowSelf.high+1 #This is so it is always outside of the range
        HighLowSelf.botGuess=HighLowSelf.guess
        HighLowSelf.output=""
        HighLowSelf.user_input=""
        HighLowSelf.enter_pressed=False
        HighLowSelf.validGuess = False
        HighLowSelf.average=0
        HighLowSelf.avgscore=[]  