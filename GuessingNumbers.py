"""GuessingNumbers by Zach Stull. The main file to host the class HighLow, which runs the game
A guessing game between you and a bot to be the first to guess the random number between 1 and 100.
 You are told if the number is higher or lower than your guess each round. There are unlimited rounds
 with feedback in between each one showing stats to make it feel more like a built out text based game.
 It was built out of Project 1 code. Alien Invasion code was used for the basic outline and frame and was left
 sitting in many commits. 11/4/26"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#    I didn't make the game look nice and pretty, or even move it away from being entirely text based,
#    but I think it's pretty decent. I definetly gained a much better understanding of pygame which will
#    hopefully come in handy with the final project.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from random import randint

import sys
from time import sleep
import pygame

#from settings import Settings
from text import Intro
from button import Button


class HighLow:
    """Class to manage overall game behavior"""
    def __init__(self):
        """Initilize the game and create game resources"""
        pygame.init()


        #SETTINGS:
        self.showBotGuess=False        
        self.low=0 #just making low and high in case I want to change it later
        self.high=100

        self._set_up_one_time_vars()
        self._set_up_every_round_vars()
        self.game_active = False       
        self.clock= pygame.time.Clock()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("High Low")
        #create an instance to display text.
        self.tut = Intro(self)
        self.bg_clr=(0,0,0)
        #make the Play button.
        self.play_button = Button(self, "Start")
        self.no_button = Button(self, "")

    def run_game(self):
        """Houses main gameloop"""
        while True:    
            if self.game_active:
                self._set_up_every_round_vars()
                while not ((self.guess == self.a) or (self.botGuess == self.a)):
                    self.botGuess=randint(self.botLow,self.botHigh)
                    if (self.botLow == self.low) & (self.botHigh == self.high): #Seeing if it is the first time in the round
                        self.guess = self.validation(True)
                    else:
                        self.guess = self.validation(False)
                    self.botGuess=randint(self.botLow,self.botHigh)
                    self.guess_analysis=self.guess_processing()
                    self.guess_display()
                if self.guess == self.a:
                    self.tut.prep_custom_text("Congrats! You won the round! :D")
                    self.scores.append(self.numGuesses)
                else:
                    self.tut.prep_custom_text("The bot won :S")
                    self.scores.append("LOST! (10)")
                self.roundsPlayed += 1
                #get average score
                self.average=0
                self.avgscore=[]
                for i in range (len(self.scores)):
                    if self.scores[i-1] == 'LOST! (10)':
                        self.avgscore.append(10)
                    else:
                        self.avgscore.append(self.scores[i-1])                                        
                for i in self.avgscore: self.average+= i
                self.average /= len(self.avgscore)
                self.tut.prep_custom_text(f"You have played {self.roundsPlayed} rounds and have gotten the following scores: \n"
                                          +(", ".join(str(i) for i in self.scores))+f"\n"
                                          +(f"Your Average Score Is {self.average:.2f} \nYour Highscore Is {min(self.avgscore)}"))
                self.refresh_screen()
                sleep(4)
                self.tut.prep_custom_text("Do you want to play again? (y/n) ")
                self.refresh_screen()
                sleep(0.5)
                self.validGuess=False
                while not self.validGuess: #Make them keep trying until they get it right
                    while not self.enter_pressed:
                        self._check_events(True)
                        if not self.user_input == "":
                            self.tut.prep_custom_text(self.user_input)
                        self.refresh_screen() 
                    self.enter_pressed=False 
                    self.guess=(self.user_input).strip()
                    self.user_input=""                
                    if self.guess== "y" or self.guess=="n":
                        self.validGuess=True
                    else:
                        self.tut.prep_custom_text(f"Your must enter y or n. \n Do you want to play again? (y/n) ")
                        self.refresh_screen()
                        sleep(1)
                self.newRound=self.guess                                     
                if self.newRound=="n":
                    self.game_active=False 
                
            else:
                self._check_events()
            
            self.refresh_screen()

    def refresh_screen(self):
        """Updates the screen"""
        #redraw the screen
        self._update_screen()                                                                                            
        #make the most recently drawn screen visible
        pygame.display.flip()
        self.clock.tick(60)      
    
    def _set_up_one_time_vars(self):
        """Sets up vars. Were you expecting smth else???"""
        #SETTING UP VARS:
        self.scores=[]
        self.roundsPlayed=0   

    def _set_up_every_round_vars(self): #I don't know if I could've made that function name any longer :B
        """Sets up vars that need reset every round"""
        self.a=randint(self.low,self.high) #Our random num for the round
        self.numGuesses=0
        self.botLow=self.low
        self.botHigh=self.high
        self.guess=self.high+1 #This is so it is always outside of the range
        self.botGuess=self.guess
        self.output=""
        self.user_input=""
        self.enter_pressed=False
        self.validGuess = False
        self.average=0
        self.avgscore=[]  

    def _check_events(self, check_str_input=False):
        """Watch for keyboard and mouse inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_no_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event,check_str_input)
            elif event.type == pygame.TEXTINPUT and check_str_input:
                self.user_input += event.text
            


    def _check_no_button(self, mouse_pos):
        """Control the no button to the setting"""
        no_button_clicked = self.no_button.rect.collidepoint(mouse_pos)
        if no_button_clicked and not self.game_active and self.play_button.msg == "Yes":
            self.game_active = True

    def _check_play_button(self, mouse_pos):
        """Control the button to start the game, progress through initial
        dialouge, and say yes to the setting"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            if self.play_button.msg == "Start":
                self.tut.prep_tut()
                self.play_button = Button(self, "Continue")
            elif self.play_button.msg=="Continue":
                self.tut.prep_custom_text("Would you like to see the bot's guesses? (y/n)")
                self.no_button = Button(self, "No", "two")
                self.play_button = Button(self, "Yes", "one")
            elif self.play_button.msg == "Yes":
                self.showBotGuess=True
                self.game_active = True           

    def _check_keydown_events(self, event, check_str_input=False):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_BACKSPACE and check_str_input:
            try:
                self.user_input = self.user_input[:-1]
            except:
                print("There were less than 1 charachters")
        elif event.key == pygame.K_RETURN and check_str_input:
            self.enter_pressed=True

    def guess_processing(self):
        """Checks guess and bot guess and sees if they were higher, lower, or right on"""
        self.numGuesses +=1
        if self.guess > self.a:
            output="high"
        elif self.guess < self.a:
            output="low"
        else:
            output="right on!"
            return(output)
        if self.botGuess > self.a:
             self.botHigh=self.botGuess-1
             self.botOutput="high"
        elif self.botGuess < self.a:
            self.botLow=self.botGuess+1
            self.botOutput="low"
        else:
            self.botOutput="right on!"
        return(output)
        
    def guess_display(self):  
        """Displays the lowdown on what you and the bot guessed"""     
        if self.showBotGuess:
            self.tut.prep_custom_text((f"You guessed {self.guess_analysis}\n")
                                                          +(f"The Bot's Guess: {self.botGuess}"+"\n")
                                                          +(f"The Bot guessed {self.botOutput}"))
        else:
            self.tut.prep_custom_text((f"You guessed {self.guess_analysis}\n")
                                              +(f"The Bot guessed {self.botOutput}"))
        self.refresh_screen()              
        sleep(2)

    def validation(self,isFirstTime):
        """Makes sure a valid positive interger is entered, and repeats if not."""
    
        self.validGuess = False
       
        self._check_events()
        if isFirstTime:
            self.tut.prep_custom_text("Enter your first guess ")
        else:
            self.tut.prep_custom_text("Enter your next guess ")
        self.refresh_screen()

        while not self.validGuess: #Make them keep trying until they get it right
            while not self.enter_pressed:
                self._check_events(True)
                if not self.user_input == "":
                    self.tut.prep_custom_text(self.user_input)
                self.refresh_screen()

            self.enter_pressed=False 
            self.guess=(self.user_input).strip()
            self.user_input=""
            #Weeding out nonnumerical inputs and negative numbers so no errors occur. Also return false with a decimal point
            if self.guess.isdigit(): 
                self.validGuess=True      
            else:
                self.tut.prep_custom_text("Your guess must be a number")                
                self.refresh_screen()
                sleep(1)
        return int(self.guess)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_clr)

        #display text
        self.tut.show_text()     
        #draw buttons if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button() 
            if self.no_button.msg != "":
                self.no_button.draw_button()
        

if __name__ == '__main__':
    #make a game instance and run
    hl=HighLow()
    hl.run_game()