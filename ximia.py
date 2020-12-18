import tkinter as tk
from PIL import ImageTk, Image
import json
import requests
from chemspipy import ChemSpider
import os

api_key = os.environ.get('CHEMSPI_API_KEY') # API key obtained from OS environment variables, should automatize in later versions


# Ximia class, the heart of the application with __init__ and the search function

class Ximia(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master       

    def search(self=None, event=None):
        root.geometry("700x350")   
        try:       
            cs = ChemSpider(api_key)
        except Exception:
            cs = "Error..."   
        search_item = str(search_box.get())
        global compound
        result = ["glucose", "ethanol", "triterpenoid"]
        #for compound in cs.search(search_item): 

        result_list = tk.Listbox(root)
        result_list.pack(padx=15, pady=15)
        for item in result:
            result_list.insert(tk.END, item)

# MAIN WINDOW

    # Main window options
root = tk.Tk() # Create Tk
root.title("XIMIA") # Window title
root.geometry("700x150") # Window size
root.resizable(width=0, height=1) #Window size and make it resizable in height
root.iconphoto(True, tk.PhotoImage(file='./icon.png')) # Top left icon
root.config(bg="#b6d6fd") #Background color
root.bind("<Return>", Ximia.search) # Bind ENTER key to search function
    
    # Search box
search_box = tk.Entry(root, width=30) # Create entrytext box for search
search_box.config(fg="black", font=("Galaxy BT", 24)) # Font color black, style and size
search_box.pack(pady=10) # Show search box

    # Search button
search_button = tk.Button(root, text="Search", command=Ximia.search) #Create search button
search_button.config(fg="black", font=("Galaxy BT", 24)) # Button style and size
search_button.pack() #Create search button
ximia = Ximia(master=root)
root.mainloop()

  