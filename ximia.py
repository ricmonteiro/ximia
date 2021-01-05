import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import requests
from chemspipy import ChemSpider
import pubchempy as pch
import os

# Class for the main frame
# App title
# Search box, field for writing the molecule to search for
# Search button, initialized in Ximia() class

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
    
        # Search button creation
        self.search_button = tk.Button(root,text="Find your molecule", command=self.on_button)
        self.search_button.config(fg="black", font=("Galaxy BT", 24))
        self.search_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.search_button.bind('<Return>', self.on_button) 

        # Search results frame and contents creation
        self.search_frame = tk.Frame(root)  
        self.var = tk.StringVar()                                   
        self.sb_y = tk.Scrollbar(self.search_frame, orient="vertical")
        self.result_list = tk.Listbox(self.search_frame, font=("Times New Roman", 20), height=15, listvariable=self.var)
        self.search_label = tk.Label(self.search_frame, text="Search results", font=("Helvetica", 18))  

        root.mainloop()

    ### CREATE SEARCH FUNCTION, ACTIVATED ON BUTTON PRESSING ###
    def on_button(self):
        search_item = self.search_box.get()
        print(search_item)

        # try to get api key
        try:
            api_key = os.environ.get("CHEMSPI_API_KEY")
            print(api_key)
        except:
            # display error message if API key is not present
            self.error_chemspi_api()

        # call search_results function with API key
        self.search_results(api_key, search_item)

    ### ERROR MESSAGE ###
    def error_chemspi_api(self):
        messagebox.showerror("Error", "There was an error getting your API key for RSC. Please provide API key in the preferences menu (from https://developer.rsc.org/apis) or perform search using only the PubChem API.")

    ### FUNCTION TO CREATE RESULTS LIST ###
    def search_results(self, api_key, search_item):

        # Search from ChemSpider API with ChemSpiPy wrapper             
        cs = ChemSpider(api_key)
        try:
            for compound in cs.search(search_item):
                compound_name = str(compound.common_name)
            print(compound_name)

        except:
            print("No resuls from the ChemSpider API")
        
        # Search from PubChem API with PubChemPy wrapper
        try:    
            result_pch = pch.get_cids(search_item, "name", record_type="3d")
            print(result_pch)                          
            results_from_pubchem = pch.Compound.from_cid(result_pch[0]).synonyms[0:20]
            print(results_from_pubchem)

        except:
            print("No resuls from the PubChem API")
        self.show_results()

    ### FUNCTION TO SHOW RESULTS ON MAIN FRAME ###
    def show_results(self):
        self.search_frame.config(bg="#b6d6fd")
        self.search_label.config(bg="#b6d6fd")
        self.result_list.config(yscrollcommand=self.sb_y.set) 
        self.sb_y.config(command=self.result_list.yview)

        self.search_frame.grid(row=3, column=0, padx=10, sticky='nsw')
        self.result_list.grid(row=4, column=0, pady=10)
        self.sb_y.grid(row=4, column=0, sticky='nse', pady=10) 
        self.search_label.grid(row=3, column=0, pady=10)

#Initiate App   
Ximia()