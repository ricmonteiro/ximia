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
        self.search_box = tk.Entry(root, width=40, justify='center', relief="raised")
        self.search_box.config(fg="black", font=("Galaxy BT", 24)) 
        self.search_box.grid(row=1, column=0, columnspan=3, padx=30, pady=5)
    
        #Search button creation
        self.search_button = tk.Button(root,text="Find your molecule", command=self.on_button)
        self.search_button.config(fg="black", font=("Galaxy BT", 24))
        self.search_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.search_button.bind('<Return>', self.on_button)  

        root.mainloop()


    ### CREATE SEARCH FUNCTION
    def on_button(self):
        search_item = self.search_box.get()
        print(search_item)
        try:
            api_key = os.environ.get("CHEMSPI_API_KEY")
            print(api_key)
        except:
            self.error_chemspi_api
    
    def error_chemspi_api():
        tk.messagebox.showerror("Title", "Message")




    ### CREATE RESULTS LIST FUNCTION
    def search_results():
        # Search from ChemSpider API with ChemSpiPy wrapper
              
        cs = ChemSpider(api_key)
        global compound_name
        try:
            for compound in cs.search(search_item):
                compound_name = str(compound.common_name)
            print(compound_name)
        except:
            print("Error...")


        return search_item
    
Ximia()
   
