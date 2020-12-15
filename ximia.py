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
     

    def search(event=None):
        search_results = tk.Tk()
        search_results.title('XIMIA - Search results')
        search_results.resizable(width=0, height=0)
        try:       
            cs = ChemSpider(api_key)
        except Exception as e:
            cs = "Error..."   
        search_item = str(search_box.get())
        global compound
        compound = cs.search(search_item) 
        text = tk.Text(search_results)
        for i in range(len(compound)):
            result_button = tk.Button(search_results, text=str(compound[i].common_name))
            result_button.config(fg="black", font=("Galaxy BT", 24))
            result_button.grid(row=i, column=0, columnspan=2) 

root = tk.Tk()
root.title("XIMIA")
root.geometry("700x150")
root.resizable(width=0, height=0)
root.iconphoto(True, tk.PhotoImage(file='./icon.png'))
root.config(bg="#b6d6fd")
root.bind("<Return>", Ximia.search)
search_box = tk.Entry(root, width=30)
search_box.grid(row=0, column=0, columnspan=2, padx=100, pady=15)
search_box.config(font=("Times New Roman", 24))

search_button = tk.Button(root, text="Search", command=Ximia.search)
search_button.config(fg="black", font=("Galaxy BT", 24))
search_button.grid(row=1, column=0, columnspan=2, padx=100, pady=8)

ximia = Ximia(master=root)
ximia.mainloop()