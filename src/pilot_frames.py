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
        self.username = make_entry(panel, 'Username', 0)
        self.username.focus_set()
        self.licenseID = make_entry(panel, 'License ID', 1)
        self.pilot_experience = make_entry(panel, 'Pilot Experience', 2)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=3, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=3, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.add_pilot_role((
            self.username.get(),
            self.licenseID.get(),
            self.pilot_experience.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=4, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.username.delete(0, 'end')
        self.licenseID.delete(0, 'end')
        self.pilot_experience.delete(0, 'end')
        