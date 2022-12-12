import tkinter as tk
import src.rse as rse
from src.utils import make_nav_button, make_header, make_entry, make_date
from src.display_view_frame import DisplayViewFrame


def make_employee_nav(parent, controller):
    nav = tk.Frame(parent)
    home_button = make_nav_button(nav, controller, None, 'Home', parent)
    home_button.grid(row=0, column=0, sticky='w')
    
    add_employee_button = make_nav_button(nav, controller, AddEmployeeFrame, 'Add', parent)
    add_employee_button.grid(row=0, column=1, sticky='w')
    
    hire_employee_button = make_nav_button(nav, controller, HireEmployeeFrame, 'Hire', parent)
    hire_employee_button.grid(row=0, column=2, sticky='w')
    make_header(nav, 'Employees')
    return nav


class AddEmployeeFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_employee_view, nav=make_employee_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Add Employee')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.username = make_entry(panel, 'Username', 0)
        self.username.focus_set()
        self.first_name = make_entry(panel, 'First Name', 1)
        self.last_name = make_entry(panel, 'Last Name', 2)
        self.address = make_entry(panel, 'Address', 3)
        self.birthdate = make_date(panel, 'Birthdate', 4)
        self.taxID = make_entry(panel, 'Tax ID', 5)
        self.hired = make_date(panel, 'Hire Date', 6)
        self.experience = make_entry(panel, 'Experience', 7)
        self.salary = make_entry(panel, 'Salary', 8)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=9, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=9, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.add_employee((
            self.username.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.address.get(),
            self.birthdate.get_date(),
            self.taxID.get(),
            self.hired.get_date(),
            self.experience.get(),
            self.salary.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=10, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.username.delete(0, 'end')
        self.first_name.delete(0, 'end')
        self.last_name.delete(0, 'end')
        self.address.delete(0, 'end')
        self.birthdate.set_date('01/01/2000')
        self.taxID.delete(0, 'end')
        self.hired.set_date('01/01/2000')
        self.experience.delete(0, 'end')
        self.salary.delete(0, 'end')
        
        
class HireEmployeeFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_employee_view, nav=make_employee_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Hire Employee')
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
        error = rse.hire_employee((
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
        