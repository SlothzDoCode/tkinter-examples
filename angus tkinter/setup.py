from tkinter import * #for some reason you need to do this to get all parts that you will need not sure why
import tkinter as tk #easier to call if shorthanded

display = tk.Tk() #creates a location for stuff to be placed
display.config(bg = "", #either use bg or background and a colour or hex code to set the background colour of the window
               ) 


#!labels
#labels are the tkinter equivelent of textboxes

label = tk.Label(bg="", #same as in config
                 fg="", #either use fg or foreground and a colour or hex code to set the text colour
                 text="", #self explanitory
                 width="", #the width of the label
                 height="", #the height of the label
                 font=("",""), #the first set of "" is the font name the second "" is for the font size
                 )

#!buttons
#buttons are buttons you click them they do something

button = tk.Button(#the entirety of the stuff in labels can go in here and does the same thing
                   command = "" #the only new thing is this, if you put a function in here, when the button is clicked it will run the function
                   )


#!ways to make stuff appear
#note - you have to pick one of these to do, cant do a mix (i think)

label.pack() #makes the label appear on screen relative to items packed earlier

button.place()#allows you to put the coordinates of where you want it to be on the screen


display.attributes('',"") #in the first set you put commands like "-fullscreen" to make it full screen (that is the main one that you will want) the second set of "" you put in a bolean statement
display.mainloop() #will create the window and all items on the display when script is run
