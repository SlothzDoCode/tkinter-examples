from tkinter import * #for some reason you need to do this to get all parts that you will need not sure why
import tkinter as tk #easier to call if shorthanded

display = tk.Tk() #creates a location for stuff to be placed

#!labels
#labels are the tkinter equivelent of textboxes

label = tk.Label(bg="", #same as in config
                 fg="", #either use fg or foreground and a colour or hex code to set the text colour
                 text="", #self explanitory
                 width="", #the width of the label
                 height="", #the height of the label
                 font=("",""), #the first set of "" is the font name the second "" is for the font size
                 )

display.mainloop() #will create the window and all items on the display when script is run

