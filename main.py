#################
# Name: github.com/batimusprime/
# Date: 4/16/18
# Program: ASCII showcase
# Purpose: Display all possible font combinations
#################

import sys
import time

#neccessary libraries
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format

#imports var fonts, avail_colors, highlights
import fonts

#define method to clear terminal line
def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()
#get sample text from user
#text = raw_input('Enter text to display: ')

#for testing purposes, remove after
text = 'Hell Oworld'
doc = open('doc.txt', 'w')
#loop through font names
for fontCount in fonts.fonts:
    
    #loop through font colors
    for colors in fonts.avail_colors:
        
        #loop through background colors
        for highlight_colors in fonts.highlights:
            
            #do the printing
            sys.stdout.write(str(cprint(figlet_format(text, font=fontCount),
               colors, highlight_colors, attrs=['dark'])))