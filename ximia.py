import tkinter as tk
from PIL import Image, ImageTk
import json
import requests
from chemspipy import ChemSpider
import pubchempy as pch
import os


# Class for the search function and button
class Search(tk.Button):
    def __init__(self,master=None,text=None):   
        tk.Button.__init__(self,master,text=text)
        self['command'] = self.search       

    def search(self):
        print("Im working")


# Class for the main frame
# App title
# Search box, field for writing the molecule to search for
# Search button, initialized in Search() class
#

class Ximia(tk.Frame):
    def __init__(self,master=None):

        # Creation and declaration of the initial frame
        tk.Frame.__init__(self,master)
        self.config(bg="#b6d6fd")

    
        # App title, to be substituted by the software official logo
        self.appTitle = tk.Label(self,text="Ximia app")
        self.appTitle.config(fg="red", bg="#b6d6fd", font=("Galaxy BT", 24, "bold"))
        self.appTitle.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


        # Search box creation and configuration
        self.search_box = tk.Entry(width=60, justify='center')
        self.search_box.config(fg="black", font=("Galaxy BT", 24)) 
        self.search_box.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

               
        #Search button creation
        self.search_button = Search(self,text="Find your molecule")
        self.search_button.config(fg="black", font=("Galaxy BT", 24))
        self.search_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# main loop function and main configurations
# main window is NOT resizable (should it be?)
# icon placement in top left corner
# background set to light blue

def main():
    root = tk.Tk()
    ximia = Ximia(master=root)
    ximia.grid()
    root.resizable(width=0, height=0) 
    root.iconphoto(True, tk.PhotoImage(file='./icon.png')) 
    root.config(bg="#b6d6fd") 
    root.mainloop()

if __name__ == '__main__':
    main()