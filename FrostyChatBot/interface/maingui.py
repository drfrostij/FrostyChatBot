###################################
#                                 #
#    Created By DrFrostij         #
#                                 #
###################################


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

##########################
# Main Startup Code Area #
##########################


def mainGUI(): 
    # This is the main GUI code area
    #https://customtkinter.tomschimansky.com/documentation/CustomTkinter.html
    #Custom Tkinter documentation
    customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
    maingui = customtkinter.CTk()  # create CTk window like you do with the Tk window
    maingui.geometry("900x800")
    maingui.title("FrostyChatBot")
    maingui.resizable(False, False)


    # PEAK GUI designing 

    # Main container of chatting 
    frame = customtkinter.CTkFrame(maingui, width=650, height=780, corner_radius=20, fg_color="#191A28")
    frame.place(relx=0.62, rely=0.5, anchor="center")
    frame.grid_columnconfigure(0, weight=1)



    chatbotpromptstextbox = customtkinter.CTkLabel(frame,text="Chatbot Prompts", width=300, height=40)
    chatbotpromptstextbox.pack()
    chatbotpromptstextbox.place(x=100, y=450)


    # Main container of creating channel NAME !!!
    frame2 = customtkinter.CTkFrame(maingui, width=220, height=100, corner_radius=20, fg_color="#191A28")
    frame2.place(relx=0.13, rely=0.075, anchor="center")

    # Main container of creating channel DESCRIPTION and list of channels !!!
    frame3 = customtkinter.CTkFrame(maingui, width=220, height=670, corner_radius=20, fg_color="#191A28")
    frame3.place(relx=0.13, rely=0.57, anchor="center")

    maingui.mainloop()


mainGUI()