import rse
import tkinter as tk

class TKWrapper(tk.Tk):
    def __init__(self, *args, title='', width=None, height=None, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(title)
        
        # Center the screen
        width = width if width else int(self.winfo_screenwidth() * 0.75)
        height = height if height else int(self.winfo_screenheight() * 0.75)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f'{width}x{height}+{x}+{y}')
        
        # Main container frame
        self.container = tk.Frame(self) 
        self.container.pack(fill='both', expand=True)
        self.container.columnconfigure(0, weight=1)
        
        self.show_frame(HomeFrame)
    
    
    def show_frame(self, F, previous=None, **kwargs):
        if previous: previous.destroy()
        frame = F(self.container, self, **kwargs)
        frame.grid(row=0, column=0, sticky='nsew')
        
        
def make_home_button(parent, controller, frame):
    home_button = tk.Button(parent, text='Home',
    command=lambda : controller.show_frame(HomeFrame, frame))
    home_button.grid(row=0, column=0, sticky='w')
    
    
def make_header(parent, text):
    header = tk.Label(parent, text=text, font='Helvetica 28 bold')
    header.grid(row=1, column=0, columnspan=parent.grid_size()[1]+1, sticky='w')
        
        
def add_entry(parent, text, row):
    entry_label = tk.Label(parent, text=text, font='Helvetica 16')
    entry_label.grid(row=row, column=0, sticky='w')
    entry = tk.Entry(parent)
    entry.grid(row=row, column=1, sticky='w')
    
    return entry


class HomeFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        panel = tk.Frame(self)
        header = tk.Label(panel, text='Drone Delivery Service', font='Helvetica 36 bold')
        
        employee_view_button = tk.Button(panel, text='Display Employees',
        command=lambda : controller.show_frame(DisplayViewFrame, self, data=rse.display_employee_view(), title='Employees'))
        employee_view_button.grid(row=1, column=0, sticky='w')
        
        add_employee_button = tk.Button(panel, text='Add Employee',
        command=lambda : controller.show_frame(AddEmployeeFrame, self))
        add_employee_button.grid(row=1, column=1, sticky='w')
        
        header.grid(row=0, column=0, pady=5, sticky='w', columnspan=panel.grid_size()[1])
        panel.pack(padx=5, pady=5, fill='x', expand=True)


class DisplayViewFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        make_home_button(nav, controller, self)
        make_header(nav, kwargs['title'])
        nav.pack(padx=5, pady=5, fill='x', expand=True)
        
        table = tk.Frame(self, relief='solid', borderwidth=1)
        for i, entry in enumerate(kwargs['data']):
            for j, value in enumerate(entry):
                table.columnconfigure(j, weight=1)
                font = ('Helvetica', 14, 'bold' if i == 0 else '')
                frame = tk.Frame(table, relief='solid', borderwidth=1)
                frame.grid(row=i, column=j, sticky='nsew')
                label = tk.Label(frame, text=value, font=font, anchor='w')
                label.pack(padx=5, pady=5, fill='x', expand=True)
        table.pack(padx=5, pady=5, fill='x', expand=True)
        
        
class AddEmployeeFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        make_home_button(nav, controller, self)
        
        employee_view_button = tk.Button(nav, text='Display Employees',
        command=lambda : controller.show_frame(DisplayViewFrame, self, data=rse.display_employee_view(), title='Employees'))
        employee_view_button.grid(row=0, column=1, sticky='w')
        
        make_header(nav, 'Add Employee')
        nav.pack(padx=5, pady=5, fill='x', expand=True)
        
        panel = tk.Frame(self)
        self.username = add_entry(panel, 'Username', 0)
        self.username.focus_set()
        self.first_name = add_entry(panel, 'First Name', 1)
        self.last_name = add_entry(panel, 'Last Name', 2)
        self.address = add_entry(panel, 'Address', 3)
        self.birthdate = add_entry(panel, 'Birthdate', 4)
        self.taxID = add_entry(panel, 'Tax ID', 5)
        self.hired = add_entry(panel, 'Hire Date', 6)
        self.experience = add_entry(panel, 'Experience', 7)
        self.salary = add_entry(panel, 'Salary', 8)
        
        add_button = tk.Button(panel, text='Add', command=self.submit)
        add_button.grid(row=9, column=0, sticky='w')
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
