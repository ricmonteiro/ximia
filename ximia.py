import tkinter as tk
from PIL import Image, ImageTk
import json
import requests
from chemspipy import ChemSpider
import pubchempy as pch
import os

# Class for the main frame
# App title
# Search box, field for writing the molecule to search for
# Search button, initialized in Search() class

class Ximia(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        root.title('XIMIA')
        root.resizable(width=0, height=0) 
        root.iconphoto(True, tk.PhotoImage(file='./icon.png')) 
        root.config(bg="#b6d6fd")
            
        # Creation and declaration of the initial frame
        tk.Frame.__init__(self)
        self.config(bg="#b6d6fd")

        # App title, to be substituted by the software official logo
        self.appTitle = tk.Label(root, text="XIMIA")
        self.appTitle.config(fg="black", bg="#b6d6fd", font=("Courier New", 54))
        self.appTitle.grid(row=0, column=0, columnspan=3, padx=10)

        # Search box creation and configuration
        self.search_box = tk.Entry(root, width=60, justify='center')
        self.search_box.config(fg="black", font=("Galaxy BT", 24)) 
        self.search_box.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
    
        #Search button creation
        self.search_button = tk.Button(root,text="Find your molecule", command=self.on_button)
        self.search_button.config(fg="black", font=("Galaxy BT", 24))
        self.search_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.search_button.bind('<Return>', self.on_button)       
        root.mainloop()

    def on_button(self):
        search_item = self.search_box.get()
        print(search_item)
        return search_item
        
Ximia()
   
