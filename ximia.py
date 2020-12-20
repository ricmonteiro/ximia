import tkinter as tk
from PIL import Image, ImageTk
import json
import requests
from chemspipy import ChemSpider
import pubchempy as pch
import os
import pandas

# Ximia class, the heart of the application with __init__ and the search function

class Ximia(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master       

    def search(self=None, event=None):
        api_key = os.environ.get("CHEMSPI_API_KEY") 
        try:       
            cs = ChemSpider(api_key)
        except Exception:
            cs = "Error..."   
        search_item = str(search_box.get())
        global compound
        result = ["glucose", "ethanol", "triterpenoid"] 
        result_pch = pch.get_compounds(result[0], "name", record_type="3d")
        print(result_pch)
        result_list = tk.Listbox(root, width=15, height=len(result))
        result_list.grid(row=3, column=0, padx=10, pady=10, sticky='w'+'e'+'n'+'s')        
        for item in result:
            result_list.insert(tk.END, item)
            
        
        #for compound in cs.search(search_item):
        #    compound_name = str(compound.common_name)
        #    result_list.insert(tk.END, compound_name)


# MAIN WINDOW

    # Main window options

root = tk.Tk() # Create Tk
root.title("XIMIA") # Window title
root.geometry() # Window size
root.resizable(width=0, height=0) #Window size and make it resizable in height
root.iconphoto(True, tk.PhotoImage(file='./icon.png')) # Top left icon
root.config(bg="#b6d6fd") #Background color
root.bind("<Return>", Ximia.search) # Bind ENTER key to search function
    

    # Search box

search_box = tk.Entry(root, width=30) # Create entrytext box for search
search_box.config(fg="black", font=("Galaxy BT", 24)) # Font color black, style and size
search_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10) # Show search box


    # Check boxes for search type

check_box_1 = tk.Checkbutton(root, text="Search ChemSpider")
check_box_1.grid(row=0, column=4)
check_box_2 = tk.Checkbutton(root, text="Search PubChem")
check_box_2.grid(row=0, column=5)


    # Search button

search_button = tk.Button(root, text="Find your molecule", command=Ximia.search) #Create search button
search_button.config(fg="black", font=("Galaxy BT", 24)) # Button style and size
search_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10) #Create search button
ximia = Ximia(master=root)
root.mainloop()