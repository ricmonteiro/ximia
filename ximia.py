import tkinter as tk
from PIL import Image, ImageTk
import json
import requests
from chemspipy import ChemSpider
import pubchempy as pch
import os

# Ximia class, the heart of the application with __init__ and the search function

class Ximia(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master   
         
    def search(self=None, event=None):
        search_frame = tk.Frame(root)
        sb_y = tk.Scrollbar(search_frame, orient="vertical")
        result_list = tk.Listbox(search_frame, font=("Times New Roman", 20), height=15)
        result_list.config(yscrollcommand=sb_y.set) 
        sb_y.config(command=result_list.yview)
        search_frame.config()
        
               
        #ChemSpider API search
        api_key = os.environ.get("CHEMSPI_API_KEY") 
        try:       
            cs = ChemSpider(api_key)
        except Exception:
            print("Error...")   
        search_item = str(search_box.get())
        global compound_name
        for compound in cs.search(search_item):
            compound_name = str(compound.common_name) 
        
        #PubChem API search
        result_pch = pch.get_cids(search_item, "name", record_type="3d")
        print(result_pch)
        results_from_pubchem = pch.Compound.from_cid(result_pch[0]).synonyms[0:20]
        print(results_from_pubchem)
        for item in results_from_pubchem:
            result_list.insert(tk.END,item)

        try:
            for item in compound_name:
                result_list.insert(tk.END, item)
        except Exception:
            print("No results were obtained from the ChemSpider APi")

        search_frame.grid(padx=10)
        result_list.grid()
        sb_y.grid(row=2, column=1, sticky="nse")
        
        

    def choose_result():
                  pass



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
search_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10) # Show search box
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