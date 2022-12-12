import tkinter as tk
import src.rse as rse
from src.utils import make_nav_button, make_header, make_entry
from src.display_view_frame import DisplayViewFrame


def make_payload_nav(parent, controller):
    nav = tk.Frame(parent)
    home_button = make_nav_button(nav, controller, None, 'Home', parent)
    home_button.grid(row=0, column=0, sticky='w')
    
    load_drone_button = make_nav_button(nav, controller, LoadDroneFrame, 'Load Drone', parent)
    load_drone_button.grid(row=0, column=1, sticky='w')
    
    purchase_ingredient_button = make_nav_button(nav, controller, PurchaseIngredientFrame, 'Purchase Ingredient', parent)
    purchase_ingredient_button.grid(row=0, column=2, sticky='w')
    make_header(nav, 'Payloads')
    return nav


class LoadDroneFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_payload_view, nav=make_payload_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Load Drone')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.id = make_entry(panel, 'Drone Id', 0)
        self.id.focus_set()
        self.tag = make_entry(panel, 'Drone Tag', 1)
        self.barcode = make_entry(panel, 'Barcode', 2)
        self.more_packages = make_entry(panel, 'Quantity', 3)
        self.price = make_entry(panel, 'Price', 4)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=5, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=5, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.load_drone((
            self.id.get(),
            self.tag.get(),
            self.barcode.get(),
            self.more_packages.get(),
            self.price.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=6, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.id.delete(0, 'end')
        self.tag.delete(0, 'end')
        self.barcode.delete(0, 'end')
        self.more_packages.delete(0, 'end')
        self.price.delete(0, 'end')
        
        
class PurchaseIngredientFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_payload_view, nav=make_payload_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Purchase Ingredient')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.long_name = make_entry(panel, 'Restaurant Name', 0)
        self.long_name.focus_set()
        self.id = make_entry(panel, 'Drone Id', 1)
        self.tag = make_entry(panel, 'Drone Tag', 2)
        self.barcode = make_entry(panel, 'Barcode', 3)
        self.quantity = make_entry(panel, 'Quantity', 4)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=5, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=5, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.purchase_ingredient((
            self.long_name.get(),
            self.id.get(),
            self.tag.get(),
            self.barcode.get(),
            self.quantity.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=6, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.long_name.delete(0, 'end')
        self.id.delete(0, 'end')
        self.tag.delete(0, 'end')
        self.barcode.delete(0, 'end')
        self.quantity.delete(0, 'end')
        