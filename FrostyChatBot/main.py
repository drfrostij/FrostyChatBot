########################
# The imports section  #
########################


import os                       # this is used to get the images + sounds we want                   # (needs pip installment)
# https://docs.python.org/3/library/os.html                                                         #OS documentation
import customtkinter as customtkinter  # this is for the GUI                                        # (needs pip installment)
#https://customtkinter.tomschimansky.com                                                            #Custom Tkinter documentation
import bcrypt                         # this is for the password hashing                            # (needs pip installment)    
#https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/                      #Bcrypt documentation
from tkinter import messagebox          # this is for small popups                                  # (needs pip installment)
#https://docs.python.org/3/library/tkinter.messagebox.html                                          #Message box documentation    
import tkinter


##############################
# Importing from other files #
##############################


#import # filename          # this is for importing all the varibles from a file

#print(#filename.variable)

from interface import logingui


##########################
# Main Startup Code Area #
##########################


def startup():
    # This is the main startup code area
    logingui.loginGUI()






##
## Code startup() is the main function that is called when the program is run. It is responsible for starting the login GUI.
##

startup()