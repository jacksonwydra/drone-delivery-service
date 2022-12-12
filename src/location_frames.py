import tkinter as tk
import src.rse as rse
from src.utils import make_nav_button, make_header, make_entry
from src.display_view_frame import DisplayViewFrame


def make_location_nav(parent, controller):
    nav = tk.Frame(parent)
    home_button = make_nav_button(nav, controller, None, 'Home', parent)
    home_button.grid(row=0, column=0, sticky='w')
    
    add_location_button = make_nav_button(nav, controller, AddLocationFrame, 'Add', parent)
    add_location_button.grid(row=0, column=1, sticky='w')
    make_header(nav, 'Locations')
    return nav


class AddLocationFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_location_view, nav=make_location_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Add Location')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.label = make_entry(panel, 'Label', 0)
        self.label.focus_set()
        self.x_coord = make_entry(panel, 'X Coord', 1)
        self.y_coord = make_entry(panel, 'Y Coord', 2)
        self.space = make_entry(panel, 'Space', 3)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=4, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=4, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.add_location((
            self.label.get(),
            self.x_coord.get(),
            self.y_coord.get(),
            self.space.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=5, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.label.delete(0, 'end')
        self.x_coord.delete(0, 'end')
        self.y_coord.delete(0, 'end')
        self.space.delete(0, 'end')
        