import tkinter as tk
import src.rse as rse
from src.utils import make_nav_button, make_header, make_entry
from src.display_view_frame import DisplayViewFrame


def make_service_nav(parent, controller):
    nav = tk.Frame(parent)
    home_button = make_nav_button(nav, controller, None, 'Home', parent)
    home_button.grid(row=0, column=0, sticky='w')
    
    add_service_button = make_nav_button(nav, controller, AddServiceFrame, 'Add', parent)
    add_service_button.grid(row=0, column=1, sticky='w')
    
    manage_service_button = make_nav_button(nav, controller, ManageServiceFrame, 'Add Manager', parent)
    manage_service_button.grid(row=0, column=2, sticky='w')
    make_header(nav, 'Services')
    return nav


class AddServiceFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_service_view, nav=make_service_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Add Service')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.id = make_entry(panel, 'Id', 0)
        self.id.focus_set()
        self.long_name = make_entry(panel, 'Long Name', 1)
        self.home_base = make_entry(panel, 'Home Base', 2)
        self.manager = make_entry(panel, 'Manager', 3)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=4, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=4, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.add_service((
            self.id.get(),
            self.long_name.get(),
            self.home_base.get(),
            self.manager.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=5, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.id.delete(0, 'end')
        self.long_name.delete(0, 'end')
        self.home_base.delete(0, 'end')
        self.manager.delete(0, 'end')
        
        
class ManageServiceFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_service_view, nav=make_service_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Add Manager')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.username = make_entry(panel, 'Employee Username', 0)
        self.username.focus_set()
        self.id = make_entry(panel, 'Service Id', 1)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=2, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=2, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.manage_service((
            self.username.get(),
            self.id.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=3, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.username.delete(0, 'end')
        self.id.delete(0, 'end')
        