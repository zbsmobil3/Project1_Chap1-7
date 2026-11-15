"""GuessingNumbers by Zach Stull. This file holds all tests, 
I looked at the textbook when making the first test, 11/4/26. """

import pygame.font
from text import Intro
pygame.init()
pygame.font.init()

class Test:

    def test_single_line_text(self):
        """Does A single line of text work?"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.intro=Intro(self)
        result=self.reg_text = self.intro.prep_custom_text("this is a regular string of text")
        assert result=="Sucsessful!"

    def test_multi_line_text(self):
        """Do multiple lines of text work?"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.intro=Intro(self)
        result=self.reg_text = self.intro.prep_custom_text(f"these are regular strings of text \n these are regular strings of text \n these are regular strings of text")
        assert result=="Sucsessful!"

    def test_numbers_text(self):
        """Do numbers work?"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.intro=Intro(self)
        result=self.reg_text = self.intro.prep_custom_text(123456789.0)
        assert result=="Sucsessful!"

    def test_special_multi_line_text(self):
        """Does no f string work?"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.intro=Intro(self)
        result=self.reg_text = self.intro.prep_custom_text("this is a regular string of text \nthis is a regular string of text \nthis is a regular string of text \n")
        assert result=="Sucsessful!"


#This fails. Now I know I can mix it up
    def test_mix_text(self):
        """Can I mix it up?"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.intro=Intro(self)
        cool_char='#'
        result=self.reg_text = self.intro.prep_custom_text(5+cool_char+"this is a regular string of text \nthis is a regular string of text")
        assert result=="Sucsessful!"

#This Passes
    def test_mix_var_and_text(self):
        """Is vars and text the problem?"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.intro=Intro(self)
        cool_char='#'
        result=self.reg_text = self.intro.prep_custom_text(cool_char+"this is a regular string of text \nthis is a regular string of text")
        assert result=="Sucsessful!"

#Now I know (as I should've remebered) that I can't add an integer (or float) to a string. It only joins with + when it
#is a string and a string or a string and a char or a string and an integer (or float) converted to a string

#Final Test. I rewrote the other and now everything works great! (I'm only leaving both in to show the process since I forgot to commit)
    def test_mix_text(self):
        """Can I mix it up?"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.intro=Intro(self)
        cool_char='#'
        result=self.reg_text = self.intro.prep_custom_text(str(5)+cool_char+"this is a regular string of text \nthis is a regular string of text")
        assert result=="Sucsessful!"