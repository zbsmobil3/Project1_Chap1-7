import pygame.font
try:
    from pygame.sprite import Group
except:
    pass

#from ship import Ship

class Intro:
    """A class to show the wall of text that is the tutorial."""

    def __init__(self, hl_game):
        """Initialize scorekeeping attributes."""
        self.hl_game = hl_game
        self.screen = hl_game.screen
        self.screen_rect = self.screen.get_rect()

        #font settings for scoring information.
        self.text_color = (100, 100, 100)
        self.font = pygame.font.SysFont(None, 48)

        #prepare the initial score image.
        self.prep_text()

    def prep_text(self):
        """Render the text"""
        text = f"self.stats.score, -1"
        self.text_image = self.font.render(text, True,
                self.text_color)

        #display the score at the top right of the screen.
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.screen_rect.center - 20
        self.text_rect.top = 20

    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.text_image, self.text_rect)
