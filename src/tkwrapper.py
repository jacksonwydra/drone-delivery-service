import rse
import tkinter as tk

class TKWrapper(tk.Tk):
    def __init__(self, *args, title='', width=None, height=None, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(title)
        
        # Center the screen
        width = width if width else int(self.winfo_screenwidth() * 0.8)
        height = height if height else int(self.winfo_screenheight() * 0.8)
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
    
    
    def show_frame(self, F, previous=None, data=None):
        if previous: previous.destroy()
        frame = F(self.container, self, data)
        frame.grid(row=0, column=0, sticky='nsew')


class HomeFrame(tk.Frame):
    def __init__(self, parent, controller, data):
        tk.Frame.__init__(self, parent)
        panel = tk.Frame(self)
        
        label = tk.Label(panel, text='Drone Delivery Service', font='Helvetica 28 bold')
        label.grid(row=0, column=0, pady=5)
        
        employee_view_button = tk.Button(panel, text='Display Employees',
        command=lambda : controller.show_frame(TableFrame, self, rse.display_employee_view()))
        employee_view_button.grid(row=1, column=0, sticky='w')
        
        panel.pack(padx=5, pady=5, fill='x', expand=True)


class TableFrame(tk.Frame):
    def __init__(self, parent, controller, data):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        home_button = tk.Button(nav, text='Home',
        command=lambda : controller.show_frame(HomeFrame, self))
        home_button.grid(row=0, column=0, sticky='nsew')
        nav.pack(padx=5, pady=5, fill='x', expand=True)
        
        table = tk.Frame(self, relief=tk.SOLID, borderwidth=1)
        for i, entry in enumerate(data):
            for j, value in enumerate(entry):
                table.columnconfigure(j, weight=1)
                font = ('Helvetica', 14, 'bold' if i == 0 else '')
                frame = tk.Frame(table, relief=tk.SOLID, borderwidth=1)
                frame.grid(row=i, column=j, sticky='nsew')
                label = tk.Label(frame, text=value, font=font, anchor='w')
                label.pack(padx=5, pady=5, fill='x', expand=True)
        table.pack(padx=5, pady=5, fill='x', expand=True)
