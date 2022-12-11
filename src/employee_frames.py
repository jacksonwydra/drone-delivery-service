import tkinter as tk
import src.rse as rse
from src.utils import make_home_button, make_header, make_entry


class AddEmployeeFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        home_button = make_home_button(nav, controller, self)
        home_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Add Employee')
        nav.pack(padx=5, pady=5, fill='x', expand=True)
        
        panel = tk.Frame(self)
        self.username = make_entry(panel, 'Username', 0)
        self.username.focus_set()
        self.first_name = make_entry(panel, 'First Name', 1)
        self.last_name = make_entry(panel, 'Last Name', 2)
        self.address = make_entry(panel, 'Address', 3)
        self.birthdate = make_entry(panel, 'Birthdate', 4)
        self.taxID = make_entry(panel, 'Tax ID', 5)
        self.hired = make_entry(panel, 'Hire Date', 6)
        self.experience = make_entry(panel, 'Experience', 7)
        self.salary = make_entry(panel, 'Salary', 8)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=9, column=0, sticky='w')
        panel.pack(padx=5, pady=5, fill='x', expand=True)
        
        
    def submit(self):
        rse.add_employee((
            self.username.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.address.get(),
            self.birthdate.get(),
            self.taxID.get(),
            self.hired.get(),
            self.experience.get(),
            self.salary.get(),
        ))
        