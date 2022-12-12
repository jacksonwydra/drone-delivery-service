import tkinter as tk
import src.rse as rse
from src.utils import make_nav_button, make_header, make_entry
from src.display_view_frame import DisplayViewFrame


def make_ingredient_nav(parent, controller):
    nav = tk.Frame(parent)
    home_button = make_nav_button(nav, controller, None, 'Home', parent)
    home_button.grid(row=0, column=0, sticky='w')
    
    add_ingredient_button = make_nav_button(nav, controller, AddIngredientFrame, 'Add', parent)
    add_ingredient_button.grid(row=0, column=1, sticky='w')
    
    remove_ingredient_button = make_nav_button(nav, controller, RemoveIngredientFrame, 'Remove', parent)
    remove_ingredient_button.grid(row=0, column=2, sticky='w')
    make_header(nav, 'Ingredients')
    return nav


class AddIngredientFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_ingredient_view, nav=make_ingredient_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Add Ingredient')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.barcode = make_entry(panel, 'Barcode', 0)
        self.barcode.focus_set()
        self.iname = make_entry(panel, 'Ingredient Name', 1)
        self.weight = make_entry(panel, 'Weight', 2)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=3, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=3, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.add_ingredient((
            self.barcode.get(),
            self.iname.get(),
            self.weight.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=4, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.barcode.delete(0, 'end')
        self.iname.delete(0, 'end')
        self.weight.delete(0, 'end')
        
        
class RemoveIngredientFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_ingredient_view, nav=make_ingredient_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Remove Ingredient')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.barcode = make_entry(panel, 'Barcode', 0)
        self.barcode.focus_set()
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=1, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=1, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.remove_ingredient((
            self.barcode.get(),
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=2, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.barcode.delete(0, 'end')
        