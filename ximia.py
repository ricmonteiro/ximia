import tkinter as tk
from PIL import Image, ImageTk
import json
import requests
from chemspipy import ChemSpider
import pubchempy as pch
import os



class Search(tk.Button):
    def __init__(self,master=None,text=None):
        tk.Button.__init__(self,master,text=text)
        self['command'] = self.search

        tk.Entry.__init__(self, width=60, justify='center')
        



    def search(self):
        print("search made")

# Class for the main frame
# It shows the app title
# 

class Ximia(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)

        self.labelHello = tk.Label(self,text="Ximia app")
        self.labelHello['fg'] = "red"
        self.labelHello.grid()

        self.search_box = Search(self) 
        self.search_box.config(fg="black", font=("Galaxy BT", 24)) 
        self.search_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10) 

        self.search_button = Search(self,text="Find your molecule")
        self.search_button.grid()


# main function and main configurations
# main window is NOT resizable
# icon placement in top left corner
# background set to light blue

def main():
    root = tk.Tk()
    ximia = Ximia(master=root)
    ximia.grid() #place ximia main window
    root.resizable(width=0, height=0) #Window size and make it resizable in height
    root.iconphoto(True, tk.PhotoImage(file='./icon.png')) # Top left icon
    root.config(bg="#b6d6fd") #Background color
    root.mainloop()

if __name__ == '__main__':
    main()