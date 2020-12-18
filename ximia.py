import tkinter as tk
from PIL import ImageTk, Image
import json
import requests
from chemspipy import ChemSpider
import os

api_key = os.environ.get('CHEMSPI_API_KEY')

class Ximia(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master       

    def search(self=None, event=None):        
        try:       
            cs = ChemSpider(api_key)
        except Exception:
            cs = "Error..."   
        search_item = str(search_box.get())
        global compound
        compound = cs.search(search_item) 
        if len(compound)>10:                      
            scroll = tk.Scrollbar(root)
            scroll.pack(side="right", fill="y")
            result = tk.Text(root, wrap=None, yscrollcommand=scroll.set)
            for i in range(len(compound)):
                result.insert("1.0", str(compound[i].common_name))           
        else:
            for i in range(len(compound)):
                result_button = tk.Button(root, text=str(compound[i].common_name))
                result_button.config(fg="black", font=("Galaxy BT", 20))
                result_button.pack(row=i+2, column=0, columnspan=2) 

root = tk.Tk()
root.title("XIMIA")
root.geometry("700x150")
root.resizable(width=0, height=1)
root.iconphoto(True, tk.PhotoImage(file='./icon.png'))
root.config(bg="#b6d6fd")
root.bind("<Return>", Ximia.search)
search_box = tk.Entry(root, width=30)
search_box.config(fg="black", font=("Galaxy BT", 24))
search_box.pack(fill=tk.Y)

search_button = tk.Button(root, text="Search", command=Ximia.search)
search_button.config(fg="black", font=("Galaxy BT", 24))
search_button.pack()

ximia = Ximia(master=root)
root.mainloop()

  