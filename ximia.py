import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import pubchempy as pch
import os
import pandas as pd

# Class for the main frame
# App title
# Search box, field for writing the molecule to search for
# Search button, initialized in Ximia() class

class Ximia(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
                           
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
        
        # Search results frame and contents creation
        self.search_frame = tk.Frame(root)  
        self.results = tk.StringVar()                                   
        self.sb_y = tk.Scrollbar(self.search_frame, orient="vertical")
        self.result_list = tk.Listbox(self.search_frame, font=("Times New Roman", 20), height=12, listvariable=self.results)
        self.search_label = tk.Label(self.search_frame, text="Search results", font=("Helvetica", 18)) 


    ### CREATE SEARCH FUNCTION, ACTIVATED ON BUTTON PRESSING ###
    def on_button(self):
        search_item = str(self.search_box.get())
        self.search_results(search_item)
    
    ### FUNCTION TO CREATE RESULTS LIST ###
    def search_results(self, search_item):
        
        # Search from PubChem API with PubChemPy wrapper #
        try:    
            result_pch = pch.get_cids(search_item, 'name', 'substance', list_return='flat')                     
            global results_from_pubchem
            #print(result_pch)
            results_from_pubchem = [pch.Compound.from_cid(res) for res in result_pch]
            #print(results_from_pubchem)
            

            # Error if there are no results
            if len(results_from_pubchem)==0:
                self.no_results()
            if len(results_from_pubchem)>0:
                self.show_results(results_from_pubchem)
            
        except:
            results_from_pubchem = []
            self.error()
            
        prop_df = pch.compounds_to_frame(results_from_pubchem) 


    ### FUNCTION THAT WARNS ABOUT NOT GETTING RESULTS ###
    def no_results(self):
        messagebox.showerror(title="No results", message="Your search yielded no results. Please search again with a different word.")

    def error(self):
        messagebox.showerror(title="Error", message="Error accessing the PubChem API")


    ### FUNCTION TO SHOW RESULTS ON MAIN FRAME ###
    def show_results(self, results):

        # Configure result list widgets
        self.search_frame.config(bg="#b6d6fd")
        self.search_label.config(bg="#b6d6fd")
        self.sb_y.config(command=self.result_list.yview)
        self.result_list.config(relief=tk.FLAT, yscrollcommand=self.sb_y.set) 
        
        # Present search results widgets on frame
        self.search_frame.grid(row=3, column=0, padx=10, sticky='nsw')
        self.result_list.grid(row=4, column=0, rowspan=10, pady=10, sticky='nsw')
        self.result_list.delete(0, tk.END)    
 
        # Print a synonym of the searched Compounds onto the results list
        for i in results:
            try:
                self.result_list.insert(tk.END, i.synonyms[0]) 
                          
            except:
                pass     
        for i in results:
            temp_name = str(i.synonyms[0])
            temp_path = 'images/' + temp_name + '.png'
            c_img = pch.download('PNG', temp_path, temp_name, 'name', overwrite=True)           

        # Mount scroll bar
        self.sb_y.grid(row=4, column=1, rowspan=10, sticky='ns', pady=10) 
        self.search_label.grid(row=3, column=0, pady=5)
        self.result_list.bind("<<ListboxSelect>>", self.show_result_details)

    ### FUNCTION THAT SHOWS THE DETAILS ON THE CURRENT MOLECULE SELECTED SEARCH RESULTS LISTBOX ###
    def show_result_details(self, event):

        # molecule image
        img_path = 'images/' + str(self.result_list.get(self.result_list.curselection())) + '.png'
        print(img_path)
        self.img = ImageTk.PhotoImage(file=img_path)

        self.canvas = tk.Canvas(self.search_frame)
        self.canvas.grid(row=4, column=8, columnspan=3)

        self.img_label = tk.Label(self.canvas, image=self.img)
        self.img_label.pack()  
        
        # molecular formula label
        self.molecular_formula_label = tk.Label(self.search_frame, font=("Times New Roman", 20), text="Molecular formula: ")
        self.molecular_formula_label.config(bg="#b6d6fd")
        self.molecular_formula_label.grid(row=12, column=8, padx=10, pady=5)

        # molecular formula text
        self.molecular_formula = tk.Text(self.search_frame, width=10, height=1, font=("Times New Roman", 20))
        self.molecular_formula.grid(row=12, column=9, padx=10, pady=5)
        self.molecular_formula.insert(tk.END, str(results_from_pubchem[self.result_list.curselection()[0]].molecular_formula))
        self.molecular_formula.config(state=tk.DISABLED)

        # molecular weight label
        self.molecular_weight_label = tk.Label(self.search_frame, font=("Times New Roman", 20), text="Molecular weight (g/mol): ")
        self.molecular_weight_label.config(bg="#b6d6fd")
        self.molecular_weight_label.grid(row=13, column=8, padx=10, pady=5)

        # molecular weight text
        self.molecular_weight = tk.Text(self.search_frame, width=10, height=1, font=("Times New Roman", 20))
        self.molecular_weight.grid(row=13, column=9, padx=10, pady=5)
        self.molecular_weight.insert(tk.END, str(results_from_pubchem[self.result_list.curselection()[0]].molecular_weight))
        self.molecular_weight.config(state=tk.DISABLED)       

#Initiate App   
if __name__ == "__main__":
    root = tk.Tk() 
    root.title('XIMIA')                                                    # Title of the window
    root.resizable(width=0, height=0)                                      # Don't allow resize of the window
    root.iconphoto(True, tk.PhotoImage(file='./icon.png'))                 # Add awesome icon, I designed it myself
    root.config(bg="#b6d6fd")                                              # Blue background
    Ximia(root)                                                            # Open class
    root.mainloop()                                                        # App loop 