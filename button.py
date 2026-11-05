"""GuessingNumbers by Zach Stull. This file holds the class Button which generates all the buttons, 
I used some starter code from Alien Invasions, 11/4/26. """

import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, hl_game, msg, two=False):
        """Initialize button attributes."""
        self.msg=msg
        self.screen = hl_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #offsets for yes/no buttons
        if two=="one":
            self.rect.x += (self.width*2)/(-3)
        elif two=="two":
            self.rect.x += (self.width*2)/3

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        try:
            self.msg_image = self.font.render(msg, True, self.text_color,
                    self.button_color)
        except:
            pass
        else:
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = self.rect.center
            return("Sucsess!")

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)