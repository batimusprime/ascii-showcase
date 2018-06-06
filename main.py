#################
# Name: github.com/batimusprime/
# Date: 4/16/18
# Program: ASCII showcase
# Purpose: Display all possible font combinations for pyfiglet
#################

import sys

#neccessary libraries

from termcolor import cprint 
from pyfiglet import figlet_format

#imports var fonts, avail_colors, highlights
import fonts

#clear terminal line
def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()

#get sample text from user
text = input('Enter text to display: ')

#loop through font names
for fontCount in fonts.fonts:
    
    #loop through font colors
    for colors in fonts.avail_colors:
        
        #loop through background colors
        for highlight_colors in fonts.highlights:
            
            #do the printing
            cprint(figlet_format(text, font=fontCount),
               colors, highlight_colors, attrs=['dark'])    
            try:
                input("Press enter to continue")
  
            except SyntaxError as err:
                print("error: {0}".format(err))
