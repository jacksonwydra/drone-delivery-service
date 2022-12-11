import tkinter as tk
import src.rse as rse
from src.display_view_frame import DisplayViewFrame
from src.employee_frames import AddEmployeeFrame
from src.utils import make_nav_button


class HomeFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        panel = tk.Frame(self)
        header = tk.Label(panel, text='Drone Delivery Service', font='Helvetica 36 bold')
        
        employee_view_button = make_nav_button(panel, controller, DisplayViewFrame, 'View Employees',
                                               data=rse.display_employee_view(), title='Employees')
        employee_view_button.grid(row=1, column=0, sticky='w')
        
        add_employee_button = make_nav_button(panel, controller, AddEmployeeFrame, text='Add Employee')
        add_employee_button.grid(row=1, column=1, sticky='w')
        
        header.grid(row=0, column=0, pady=5, sticky='w', columnspan=panel.grid_size()[1]+1)
        panel.pack(padx=5, pady=5, fill='x', expand=True)
