"""A guessing game between you and a bot to be the first to guess the random number between 1 and 100.
 You are told if the number is higher or lower than your guess each round. There are unlimited rounds
 with feedback in between each one showing stats to make it feel more like a built out text based game."""

from random import randint

#Declaring Initial Vars/Lists
scores=[]
roundsPlayed=0
showBotGuess=False


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
            self._check_events()
            #if self.game_active:
                #self.ship.update()
                #self._update_bullets()
                #self._update_aliens()
            
            #redraw the screen
            self._update_screen()
            
            #make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        """Watch for keyboard and mouse inputs"""
        for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_no_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            #elif event.type == pygame.KEYUP:
                #self._check_keyup_events(event)

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
            

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        #if event.key == pygame.K_RIGHT:
            #self.ship.moving_right = True
        #elif event.key == pygame.K_LEFT:
            #self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        #elif event.key == pygame.K_SPACE:
            #self._fire_bullet()

    #def _check_keyup_events(self, event):
        #"""Respond to key releases."""
        #if event.key == pygame.K_RIGHT:
            #self.ship.moving_right = False
        #elif event.key == pygame.K_LEFT:
            #self.ship.moving_left = False


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

    #def _fire_bullet(self):
        #"""Create a new bullet and add it to the bullets group."""
        #if len(self.bullets) < self.settings.bullets_allowed:
            #new_bullet = Bullet(self)
            #self.bullets.add(new_bullet)

    #def _update_bullets(self):
        #"""Update position of bullets and get rid of old bullets."""
        #update bullet positions.
        #self.bullets.update()

        #get rid of bullets that have disappeared.
        #for bullet in self.bullets.copy():
            #if bullet.rect.bottom <= 0:
                 #self.bullets.remove(bullet)

        #self._check_bullet_alien_collisions()

    #def _check_bullet_alien_collisions(self): #one of the most important functions by far
        #"""Respond to bullet-alien collisions."""
        #remove any bullets and aliens that have collided.
        #collisions = pygame.sprite.groupcollide(
                #self.bullets, self.aliens, True, True)

        #if collisions:
            #for aliens in collisions.values():
                #self.stats.score += self.settings.alien_points * len(aliens)
            #self.stats.score += self.settings.alien_points
            #self.tut.prep_score()
            #self.tut.check_high_score()

        #if not self.aliens:
            #destroy existing bullets and create new fleet.
            #self.bullets.empty()
            #self._create_fleet()
            #self.settings.increase_speed()
            #increase level.
            #self.stats.level += 1
            #self.tut.prep_level()

    #def _update_aliens(self):
        #"""Check if the fleet is at an edge, then update positions."""
        #self._check_fleet_edges()
        #self.aliens.update()

        #look for alien-ship collisions.
        #if pygame.sprite.spritecollideany(self.ship, self.aliens):
            #self._ship_hit()

        #look for aliens hitting the bottom of the screen.
        #self._check_aliens_bottom()           

    #def _check_fleet_edges(self):
        #"""Respond appropriately if any aliens have reached an edge."""
        #for alien in self.aliens.sprites():
            #if alien.check_edges():
                #self._change_fleet_direction()
                #break

    #def _check_aliens_bottom(self):
        #"""Check if any aliens have reached the bottom of the screen."""
        #for alien in self.aliens.sprites():
            #if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                #self._ship_hit()
                #break

    #def _change_fleet_direction(self):
        #"""Drop the entire fleet and change the fleet's direction."""
        #for alien in self.aliens.sprites():
            #alien.rect.y += self.settings.fleet_drop_speed
        #self.settings.fleet_direction *= -1

    #def _ship_hit(self):
        #"""Respond to the ship being hit by an alien."""
        #if self.stats.ships_left > 0:

            #decrement ships_left and update scoreboard.
            #self.stats.ships_left -= 1
            #self.tut.prep_ships()

            #get rid of any remaining bullets and aliens.
            #self.bullets.empty()
            #self.aliens.empty()

            #create a new fleet and center the ship.
            #self._create_fleet()
            #self.ship.center_ship()

            #sleep(0.5) #pause.
        #else:
            #I'll probably put this in its own func for the final project
            #For readability as a end of wave sort of thing. Abstraction.
            #self.game_active = False
            #pygame.mouse.set_visible(True)

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

#13 Lines Through TOT

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
        if showBotGuess:
            print(f"The Bot's Guess: {botGuess}")
        print(f"The Bot guessed {botOutput}")
    if guess == a:
         print("Congrats! You won the round! :D")
    else:
         print("The bot won :S")

    #Highscore logic will probably go here
    global roundsPlayed
    roundsPlayed += 1
    global scores
    if guess==a:
        scores.append(numGuesses)
    else:
         scores.append("LOST! (10)")

    #Get average score
    average=0
    avgscore=[]
    for i in range (len(scores)):
        if scores[i-1] == 'LOST! (10)':
            avgscore.append(10)
        else:
             avgscore.append(scores[i-1])
             

    for i in avgscore: average+= i
    average /= len(avgscore)

    #Output
    print(f"You have played {roundsPlayed} rounds and have gotten the following scores:")
    print(*(str(i) for i in scores), sep=", ")
    print(f"Your Average Score Is {average:.2f} and Your Highscore Is {min(avgscore)}")

    newRound=input("Do you want to play again? (y/n) ")
    if newRound=="y":
         round()

#Main Body of Code
round()   
        
