import tkinter as tk
import src.rse as rse
from src.display_view_frame import DisplayViewFrame
from src.utils import make_nav_button
from src.owner_frames import make_owner_nav
from src.employee_frames import make_employee_nav
from src.pilot_frames import make_pilot_nav
from src.location_frames import make_location_nav
from src.ingredient_frames import make_ingredient_nav
from src.service_frames import make_service_nav


class HomeFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        panel = tk.Frame(self)
        header = tk.Label(panel, text='Drone Delivery Service', font='Helvetica 36 bold')
        
        owner_view_button = make_nav_button(panel, controller, DisplayViewFrame, 'View Owners', self,
                                               data=rse.display_owner_view, nav=make_owner_nav)
        owner_view_button.grid(row=1, column=0, sticky='w')
        
        employee_view_button = make_nav_button(panel, controller, DisplayViewFrame, 'View Employees', self,
                                               data=rse.display_employee_view, nav=make_employee_nav)
        employee_view_button.grid(row=2, column=0, sticky='w')
        
        pilot_view_button = make_nav_button(panel, controller, DisplayViewFrame, 'Pilots', self,
                                               data=rse.display_pilot_view, nav=make_pilot_nav)
        pilot_view_button.grid(row=3, column=0, sticky='w')
        
        location_view_button = make_nav_button(panel, controller, DisplayViewFrame, 'Locations', self,
                                               data=rse.display_location_view, nav=make_location_nav)
        location_view_button.grid(row=4, column=0, sticky='w')
        
        ingredient_view_button = make_nav_button(panel, controller, DisplayViewFrame, 'Ingredients', self,
                                               data=rse.display_ingredient_view, nav=make_ingredient_nav)
        ingredient_view_button.grid(row=5, column=0, sticky='w')
        
        service_view_button = make_nav_button(panel, controller, DisplayViewFrame, 'Services', self,
                                               data=rse.display_service_view, nav=make_service_nav)
        service_view_button.grid(row=6, column=0, sticky='w')
        
        header.grid(row=0, column=0, pady=5, sticky='w', columnspan=panel.grid_size()[1]+1)
        panel.pack(padx=5, pady=5, fill='both', expand=True)
