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
    
    takeover_drone_button = make_nav_button(nav, controller, TakeoverDroneFrame, 'Takeover', parent)
    takeover_drone_button.grid(row=0, column=2, sticky='w')
    
    join_swarm_button = make_nav_button(nav, controller, JoinSwarmFrame, 'Join Swarm', parent)
    join_swarm_button.grid(row=0, column=3, sticky='w')
    
    leave_swarm_button = make_nav_button(nav, controller, LeaveSwarmFrame, 'Leave Swarm', parent)
    leave_swarm_button.grid(row=0, column=4, sticky='w')
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
        

class TakeoverDroneFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_drone_view, nav=make_drone_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Takeover Drone')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.username = make_entry(panel, 'Pilot Username', 0)
        self.username.focus_set()
        self.id = make_entry(panel, 'Drone Id', 1)
        self.tag = make_entry(panel, 'Drone Tag', 2)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=3, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=3, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.takeover_drone((
            self.username.get(),
            self.id.get(),
            self.tag.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=4, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.username.delete(0, 'end')
        self.id.delete(0, 'end')
        self.tag.delete(0, 'end')
        
        
class JoinSwarmFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_drone_view, nav=make_drone_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Join Swarm')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.id = make_entry(panel, 'Drone Id', 0)
        self.id.focus_set()
        self.tag = make_entry(panel, 'Drone Tag', 1)
        self.swarm_leader_tag = make_entry(panel, 'Swarm Leader Tag', 2)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=3, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=3, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.join_swarm((
            self.id.get(),
            self.tag.get(),
            self.swarm_leader_tag.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=4, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.id.delete(0, 'end')
        self.tag.delete(0, 'end')
        self.swarm_leader_tag.delete(0, 'end')
        
        
class LeaveSwarmFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        self.back_button = make_nav_button(nav, controller, DisplayViewFrame, 'Back', self,
                                      data=rse.display_drone_view, nav=make_drone_nav)
        self.back_button.grid(row=0, column=0, sticky='w')
        
        make_header(nav, 'Leave Swarm')
        nav.pack(padx=5, pady=5, fill='both', expand=True)
        
        panel = tk.Frame(self)
        self.id = make_entry(panel, 'Drone Id', 0)
        self.id.focus_set()
        self.tag = make_entry(panel, 'Drone Tag', 1)
        
        submit_button = tk.Button(panel, text='Submit', command=self.submit)
        submit_button.grid(row=2, column=0, sticky='w')
        clear_button = tk.Button(panel, text='Clear', command=self.clear)
        clear_button.grid(row=2, column=1, sticky='w')
        self.error = tk.StringVar()
        self.error_box = tk.Label(panel, textvariable=self.error, fg='red')
        panel.pack(padx=5, pady=5, fill='both', expand=True)
        
        
    def submit(self):
        error = rse.leave_swarm((
            self.id.get(),
            self.tag.get()
        ))
        if error:
            self.error.set(error)
            self.error_box.grid(row=3, column=0, columnspan=3, sticky='w')
        else:
            self.back_button.invoke()
        
        
    def clear(self):
        self.id.delete(0, 'end')
        self.tag.delete(0, 'end')
        