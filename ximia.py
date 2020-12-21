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
        result_pch = pch.get_compounds(search_item, "name", record_type="3d")
        print(result_pch)
        for compound in cs.search(search_item):
            compound_name = str(compound.common_name) 
            result_list = tk.Listbox(root, width=15, height=len(result))
            result_list.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='w'+'e'+'n'+'s')        
            result_list.insert(tk.END, str(result_pch[0].iupac_name))
            
            
              
# MAIN WINDOW

    # Main window options

root = tk.Tk() # Create Tk
root.title("XIMIA") # Window title
root.geometry() # Window size
root.resizable(width=0, height=0) #Window size and make it resizable in height
root.iconphoto(True, tk.PhotoImage(file='./icon.png')) # Top left icon
root.config(bg="#b6d6fd") #Background color

    # Ximia logo
#logo = ImageTk.PhotoImage(Image.open()
#logo.grid(row=0, column=0)


    # Search box

search_box = tk.Entry(root, width=30) # Create entrytext box for search
search_box.config(fg="black", font=("Galaxy BT", 24)) # Font color black, style and size
search_box.grid(row=0, column=1, columnspan=3, padx=10, pady=10) # Show search box
print("search box created")

    # Check boxes for search type 

chems_search_var = tk.StringVar() 
check_box_1 = tk.Checkbutton(root, text="Search ChemSpider", variable=chems_search_var,activebackground="#b6d6fd")
check_box_1.grid(row=0, column=5)
check_box_1.config(bg="#b6d6fd")
check_box_1.deselect()

print("checkbox 1 created")

pubchem_search_var = tk.StringVar() 
check_box_2 = tk.Checkbutton(root, text="Search PubChem", variable=pubchem_search_var, activebackground="#b6d6fd")
check_box_2.grid(row=0, column=6,padx=10)
check_box_2.config(bg="#b6d6fd")
check_box_2.deselect()

print("checkbox 2 created")


root.bind("<Return>", Ximia.search) # Bind ENTER key to search function


print("Enter key bind implemented")

    # Search button

search_button = tk.Button(root, text="Find your molecule", command=Ximia.search) #Create search button
search_button.config(fg="black", font=("Galaxy BT", 24)) # Button style and size
search_button.grid(row=1, column=1, columnspan=3, padx=10, pady=10) #Create search button

print("Search button created")
ximia = Ximia(master=root)

###tests
root.mainloop()



