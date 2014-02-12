#Henry Lee
#I did not recieve any help on the programming (other Professor Shannon's help)
#but did recieve help in testing and in the drawing of objects used in the
#second section of the game.

#This is the entire game. The import statements read in each of the three parts
#and plays them in sequence.
#All functionality is handled within their individual sections.

from intro import *
from customizationv2 import *
from main_game_screen import *

main_char=main1() #intro, passes on the Person object
main2() #customization
main3(main_char) #main game, uses the Person object
