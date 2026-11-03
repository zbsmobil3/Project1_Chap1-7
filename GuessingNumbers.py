"""A guessing game between you and a bot to be the first to guess the random number between 1 and 100.
 You are told if the number is higher or lower than your guess each round. There are unlimited rounds
 with feedback in between each one showing stats to make it feel more like a built out text based game."""

from random import randint

#-------------------------------------------------------------------------------------------------------------
import sys
from time import sleep
import pygame

#from settings import Settings
#from game_stats import GameStats
from Tutorial import Intro
from button import Button
#from ship import Ship
#from bullet import Bullet
#from alien import Alien


class HighLow:
    """Class to manage overall game behavior"""
    def __init__(self):
        """Initilize the game and create game resources"""
        pygame.init()


        #SETTINGS:
        self.showBotGuess=False        
        self.low=0 #Just making low and high in case I want to change it later
        self.high=100
          
        
        #SETTING UP VARS:
        self.scores=[]
        self.roundsPlayed=0
        self.a=randint(self.low,self.high) #Our random num for the round
        self.numGuesses=0
        self.botLow=self.low
        self.botHigh=self.high
        self.guess=self.high+1 #This is so it is always outside of the range
        self.output=""
        self.user_input=""
        self.enter_pressed=False
        self.validGuess = False
        self.average=0
        self.avgscore=[]

        #start Alien Invasion in an inactive state.
        self.game_active = False
        
        self.clock= pygame.time.Clock()
        #self.settings=Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height


        pygame.display.set_caption("High Low")
        #i'll probably create an icon here later

        #create an instance to store game statistics, and create a scoreboard.
        #self.stats = GameStats(self)
        self.tut = Intro(self)

        self.bg_clr=(0,0,0)

        #self.ship=Ship(self)
        #self.bullets = pygame.sprite.Group()
        #self.aliens = pygame.sprite.Group()

        #self._create_fleet()

        #make the Play button.
        self.play_button = Button(self, "Start")
        self.no_button = Button(self, "")

    def run_game(self):
        """Houses main gameloop"""

        while True:    
            if self.game_active:
                while not ((self.guess == self.a) or (self.guess == self.a)):
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
                self.tut.show_text()
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


                
            else:
                self._check_events()
                #self.ship.update()
                #self._update_bullets()
                #self._update_aliens()
            
            #redraw the screen
            self._update_screen()
            
            #make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self, check_str_input=False):
        """Watch for keyboard and mouse inputs"""
        for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_no_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event,check_str_input)
            #elif event.type == pygame.KEYUP:
                #self._check_keyup_events(event)
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
                self.tut.prep_setting_choice()
                self.no_button = Button(self, "No", "two")
                self.play_button = Button(self, "Yes", "one")
            elif self.play_button.msg == "Yes":
                self.showBotGuess=True
                self.game_active = True

            #hide the mouse cursor.
            #pygame.mouse.set_visible(False)
            

    def _check_keydown_events(self, event, check_str_input=False):
        """Respond to keypresses."""
        #if event.key == pygame.K_RIGHT:
            #self.ship.moving_right = True
        #elif event.key == pygame.K_LEFT:
            #self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_BACKSPACE and check_str_input:
            try:
                self.user_input = self.user_input[:-1]
            except:
                print("There were less than 1 charachters")
        elif event.key == pygame.K_RETURN and check_str_input:
            self.enter_pressed=True

        #elif event.key == pygame.K_SPACE:
            #self._fire_bullet()

    #def _check_keyup_events(self, event):
        #"""Respond to key releases."""
        #if event.key == pygame.K_RIGHT:
            #self.ship.moving_right = False
        #elif event.key == pygame.K_LEFT:
            #self.ship.moving_left = False

    def guess_processing(self):
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
        self.tut.prep_custom_text(f"You guessed {self.guess_analysis}")
        #redraw the screen
        self._update_screen()
                                                                            
        #make the most recently drawn screen visible
        pygame.display.flip()
        self.clock.tick(60)
        
        sleep(0.5)
        if self.showBotGuess:
            self.tut.prep_custom_text(f"The Bot's Guess: {self.botGuess}")
                    #redraw the screen
            self._update_screen()
                                                                            
            #make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)
        
            sleep(0.5)
        self.tut.prep_custom_text(f"The Bot guessed {self.botOutput}")
                #redraw the screen
        self._update_screen()
                                                                            
        #make the most recently drawn screen visible
        pygame.display.flip()
        self.clock.tick(60)
        
        sleep(0.5)


    def validation(self,isFirstTime): #Created to not go more than 3 deep
        """Makes sure a valid positive interger is entered, and repeats if not."""
    
        self.validGuess = False
       
        self._check_events()
        if isFirstTime:
            self.tut.prep_custom_text("Enter your first guess ")
        else:
            self.tut.prep_custom_text("Enter your next guess ")
        #redraw the screen
        self._update_screen()
                                                                    
        #make the most recently drawn screen visible
        pygame.display.flip()
        self.clock.tick(60)

        sleep(0.5)

        while not self.validGuess: #Make them keep trying until they get it right
            while not self.enter_pressed:
                self._check_events(True)
                if not self.user_input == "":
                    self.tut.prep_custom_text(self.user_input)
                #redraw the screen
                self._update_screen()
                                                    
                #make the most recently drawn screen visible
                pygame.display.flip()
                self.clock.tick(60)
                #self.guess=input("Enter your first guess ").strip() 
            self.enter_pressed=False 

            self.guess=(self.user_input).strip()
            self.user_input=""
            
            #self.guess=input("Enter your next guess ").strip()         
            if self.guess.isdigit(): #Weeding out nonnumerical inputs and negative numbers so no errors occur. Also return false with a decimal point
                self.validGuess=True
            else:
                self.tut.prep_custom_text("Your guess must be a number")
                
                #redraw the screen
                self._update_screen()
                                                                                    
                #make the most recently drawn screen visible
                pygame.display.flip()
                self.clock.tick(60)
                sleep(1)
        return int(self.guess)



    #def _create_fleet(self):
        #"""Create the fleet of aliens."""
        #create an alien and keep adding aliens until there's no room left.
        #spacing between aliens is one alien width and one alien height.
        #alien = Alien(self)
        #alien_width, alien_height = alien.rect.size

        #current_x, current_y = alien_width, alien_height
        #while current_y < (self.settings.screen_height - 3 * alien_height):
            #while current_x < (self.settings.screen_width - 2 * alien_width):
                #self._create_alien(current_x, current_y)
                #current_x += 2 * alien_width

            #finished a row; reset x value, and increment y value.
            #current_x = alien_width
            #current_y += 2 * alien_height

    #def _create_alien(self, x_position, y_position):
        #"""Create an alien and place it in the fleet."""
        #new_alien = Alien(self)
        #new_alien.x = x_position
        #new_alien.rect.x = x_position
        #new_alien.rect.y = y_position
        #self.aliens.add(new_alien)         



    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_clr)
        #for bullet in self.bullets.sprites():
            #bullet.draw_bullet()
        #self.ship.blitme()
        #self.aliens.draw(self.screen)

        #draw the score information.
        self.tut.show_text()
        
        #draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button() 
            if self.no_button.msg != "":
                self.no_button.draw_button()
        

if __name__ == '__main__':
    #make a game instance and run
    hl=HighLow()
    hl.run_game()
#-------------------------------------------------------------------------------------------------------------

#82 Lines Through T-T

#Just some welcome and setting(s)
#print()
#print("Welcome to the Number Guessing Game!")
#print("Each Round you try to guess a number between 1 and 100")
#print("And get told whether you guessed above or below the number")
#print("You are guessing against a bot")
#input("Press enter to continue ")
#print()
#z=input("Would you like to see the bot's guesses? (y/n) ")
#if z=="y":
#    showBotGuess=True
#
#def validation(isFirstTime): #Created to not go more than 3 deep
#    """Makes sure a valid positive interger is entered, and repeats if not."""
#    
#    validGuess = False
#    while validGuess != True: #Make them keep trying until they get it right
#                if isFirstTime:
#                     guess=input("Enter your first guess ").strip()         
#                else:
#                     guess=input("Enter your next guess ").strip()                 
#                if guess.isdigit(): #Weeding out nonnumerical inputs and negative numbers so no errors occur. Also return false with a decimal point
#                    validGuess=True
#                else:
#                    print("Your guess must be a number")
#    return int(guess)


def round ():
    """The Core Loop, run each Round"""

    #numGuesses=0
    #low=0 #Just making low and high in case I want to change it later
    #high=100
    #a=randint(low,high) #Our random num for the round

    #botLow=low
    #botHigh=high

  

    #guess=high+1 #This is so it is always outside of the range
    #output=""

    #while guess != a: #This isn't really needed since I'm using a break instead.
        #botGuess=randint(botLow,botHigh)
        #if (botLow == low) & (botHigh == high): #Seeing if it is the first time in the round
        #    guess = validation(True)
        #else:
        #    guess = validation(False)
        #numGuesses +=1
        #if guess > a:
        #    output="high"
        #elif guess < a:
        #    output="low"
        #else:
        #    output="right on!"
        #    break
        #if botGuess > a:
        #     botHigh=botGuess-1
        #     botOutput="high"
        #elif botGuess < a:
        #    botLow=botGuess+1
        #    botOutput="low"
        #else:
        #    break
        #print(f"You guessed {output}")
        #if showBotGuess:
        #    print(f"The Bot's Guess: {botGuess}")
        #print(f"The Bot guessed {botOutput}")
    #if guess == a:
    #     print("Congrats! You won the round! :D")
    #else:
    #     print("The bot won :S")

    #Highscore logic will probably go here
    #global roundsPlayed
    #roundsPlayed += 1
    #global scores
    #if guess==a:
    #    scores.append(numGuesses)
    #else:
    #     scores.append("LOST! (10)")

    #Get average score
    #average=0
    #avgscore=[]
    #for i in range (len(scores)):
    #    if scores[i-1] == 'LOST! (10)':
    #        avgscore.append(10)
    #    else:
    #         avgscore.append(scores[i-1])
             

    #for i in avgscore: average+= i
    #average /= len(avgscore)

    #Output
    print(f"You have played {roundsPlayed} rounds and have gotten the following scores:")
    print(*(str(i) for i in scores), sep=", ")
    print(f"Your Average Score Is {average:.2f} and Your Highscore Is {min(avgscore)}")

    newRound=input("Do you want to play again? (y/n) ")
    if newRound=="y":
         round()

#Main Body of Code
round()   
        
