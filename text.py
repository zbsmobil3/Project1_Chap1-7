"""GuessingNumbers by Zach Stull. This file holds the intro class which handles all my text,
some starter code was used from alien invasion. It's definetly changed since then, 11/4/26. """


try:
    import pygame.font
except:
    pass

class Intro:
    """A class to show the wall of text that is the tutorial."""

    def __init__(self, hl_game):
        """Initialize scorekeeping attributes."""
        self.tut_lines=["Welcome to the Number Guessing Game!","Each Round you try to guess a number between 1 and 100","And get told whether you guessed above or below the number","You are guessing against a bot","Press button to continue"]

        self.hl_game = hl_game
        self.screen = hl_game.screen
        self.screen_rect = self.screen.get_rect()

        #font settings for scoring information.
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 48)

        #prepare the initial score image.
        self.text_image = self.font.render("", True,
                        self.text_color)
        self.text_rect = self.text_image.get_rect()

    def prep_custom_text(self, text):
        """Render the text"""
        try:
            self.text_image = self.font.render(f"{text}", True,
                   self.text_color)
        except:
            return("fail")
        else:
            #display the score at the top right of the screen.
            self.text_rect = self.text_image.get_rect()
            self.text_rect.center = self.screen_rect.center
            self.text_rect.top = 20
            return("Sucsessful!")
        
    def prep_tut(self):
        """Render the text"""
        text=""
        for i in self.tut_lines:
            text+=str("\n"+i)
        self.text_image = self.font.render(f"{text}", True,
                self.text_color)

        #display the score at the top right of the screen.
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.screen_rect.center
        self.text_rect.top = 20

    def show_text(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.text_image, self.text_rect)
