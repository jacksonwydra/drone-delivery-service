import tkinter as tk
import src.rse as rse
from src.utils import make_nav_button, make_header, make_entry
from src.display_view_frame import DisplayViewFrame


def make_pilot_nav(parent, controller):
    nav = tk.Frame(parent)
    home_button = make_nav_button(nav, controller, None, 'Home', parent)
    home_button.grid(row=0, column=0, sticky='w')
    
    add_pilot_button = make_nav_button(nav, controller, AddPilotFrame, 'Add', parent)
    add_pilot_button.grid(row=0, column=1, sticky='w')
    make_header(nav, 'Pilots')
    return nav


class AddPilotFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_pilot_view, nav=make_pilot_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Add Pilot')
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
        rse.add_pilot((
            self.name.get()
        ))
        self.back_button.invoke()
        
        
    def clear(self):
        self.name.delete(0, 'end')
        