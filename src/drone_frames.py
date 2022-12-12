import tkinter as tk
import src.rse as rse
from src.utils import make_nav_button, make_header, make_entry
from src.display_view_frame import DisplayViewFrame


def make_drone_nav(parent, controller):
    nav = tk.Frame(parent)
    home_button = make_nav_button(nav, controller, None, 'Home', parent)
    home_button.grid(row=0, column=0, sticky='w')
    
    add_drone_button = make_nav_button(nav, controller, AddDroneFrame, 'Add', parent)
    add_drone_button.grid(row=0, column=1, sticky='w')
    make_header(nav, 'Drones')
    return nav


class AddDroneFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_drone_view, nav=make_drone_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Add Drone')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.id = make_entry(panel, 'Id', 0)
        self.id.focus_set()
        self.tag = make_entry(panel, 'Tag', 1)
        self.fuel = make_entry(panel, 'Fuel', 2)
        self.capacity = make_entry(panel, 'Capacity', 3)
        self.sales = make_entry(panel, 'Sales', 4)
        self.flown_by = make_entry(panel, 'Flown By', 5)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=6, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=6, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.add_drone((
            self.id.get(),
            self.tag.get(),
            self.fuel.get(),
            self.capacity.get(),
            self.sales.get(),
            self.flown_by.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=7, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.id.delete(0, 'end')
        self.tag.delete(0, 'end')
        self.fuel.delete(0, 'end')
        self.capacity.delete(0, 'end')
        self.sales.delete(0, 'end')
        self.flown_by.delete(0, 'end')
        