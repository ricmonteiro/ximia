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

def search():
    search_results = tk.Tk()
    search_results.title('XIMIA - Search results')
    search_results.geometry("380x400")
    search_results.resizable(width=0, height=0)
    try:       
        cs = ChemSpider(api_key)
    except Exception as e:
        cs = "Error..."   
    search_item = str(search_box.get())
    print(search_item)
    compound = cs.search(search_item) 
    print(compound)
    text = tk.Text(search_results)
    print(compound[0].common_name)
    for i in range(len(compound)):
        text.insert(tk.INSERT, compound[i].common_name + '\n')
        text.grid(row=i, column=0)
        text.insert(tk.INSERT, compound[i].molecular_formula + '\n')
        text.grid(row=i, column=1)
        text.insert(tk.INSERT, str(compound[i].molecular_weight) + '\n')
        text.grid(row=i, column=2) 

root = tk.Tk()
root.title("XIMIA")
root.geometry("380x50")
root.resizable(width=0, height=0)
search_box = tk.Entry(root, width=30)
search_box.grid(row=0, column=0, columnspan=2, padx=100)
search_button = tk.Button(root, text="Search", command=search)
search_button.grid(row=1, column=0, columnspan=2, padx=100)

ximia = Ximia(master=root)
ximia.mainloop()