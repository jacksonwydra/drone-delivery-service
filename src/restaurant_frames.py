import tkinter as tk
import src.rse as rse
from src.utils import make_nav_button, make_header, make_entry
from src.display_view_frame import DisplayViewFrame


def make_restaurant_nav(parent, controller):
    nav = tk.Frame(parent)
    home_button = make_nav_button(nav, controller, None, 'Home', parent)
    home_button.grid(row=0, column=0, sticky='w')
    
    add_restaurant_button = make_nav_button(nav, controller, AddRestaurantFrame, 'Add', parent)
    add_restaurant_button.grid(row=0, column=1, sticky='w')
    
    start_funding_button = make_nav_button(nav, controller, StartFundingFrame, 'Start Funding', parent)
    start_funding_button.grid(row=0, column=2, sticky='w')
    make_header(nav, 'Restaurants')
    return nav


class AddRestaurantFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_restaurant_view, nav=make_restaurant_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Add Restaurant')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.long_name = make_entry(panel, 'Long Name', 0)
        self.long_name.focus_set()
        self.rating = make_entry(panel, 'Rating', 1)
        self.spent = make_entry(panel, 'Spent', 2)
        self.location = make_entry(panel, 'Location', 3)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=4, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=4, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.add_restaurant((
            self.long_name.get(),
            self.rating.get(),
            self.spent.get(),
            self.location.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=5, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.long_name.delete(0, 'end')
        self.rating.delete(0, 'end')
        self.spent.delete(0, 'end')
        self.location.delete(0, 'end')
        
        
class StartFundingFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_restaurant_view, nav=make_restaurant_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Start Funding')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.owner = make_entry(panel, 'Owner Username', 0)
        self.owner.focus_set()
        self.long_name = make_entry(panel, 'Restaurant Long Name', 1)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=2, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=2, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.start_funding((
            self.owner.get(),
            self.long_name.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=3, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.owner.delete(0, 'end')
        self.long_name.delete(0, 'end')
        