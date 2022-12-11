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
    make_header(nav, 'Ingredients')
    return nav


class AddIngredientFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_ingredient_view(), nav=make_ingredient_nav)
        back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Add Ingredient')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.name = make_entry(panel, 'Name', 0)
        self.name.focus_set()
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=1, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=1, column=1, sticky='w')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        rse.add_ingredient((
            self.name.get()
        ))
        
        
    def clear(self):
        self.name.delete(0, 'end')
        