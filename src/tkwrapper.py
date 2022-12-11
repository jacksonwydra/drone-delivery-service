import tkinter as tk
from src.home_frame import HomeFrame


class TKWrapper(tk.Tk):
    def __init__(self, *args, title='', **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(title)
        
        # Center the screen
        width = int(self.winfo_screenwidth() * 0.75)
        height = int(self.winfo_screenheight() * 0.75)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f'{width}x{height}+{x}+{y}')
        
        # Main container frame
        self.container = tk.Frame(self)
        self.container.pack(fill='both', expand=True)
        self.container.columnconfigure(0, weight=1)
        
        self.home_frame = HomeFrame(self.container, self)
        self.home_frame.grid(row=0, column=0, sticky='nsew')
    
    
    def show_frame(self, F, previous, **kwargs):
        if previous is self.home_frame:
            self.home_frame.forget()
        elif previous:
            previous.destroy()
        
        if F:
            frame = F(self.container, self, **kwargs)
            frame.grid(row=0, column=0, sticky='nsew')
        else:
            self.home_frame.grid(row=0, column=0, sticky='nsew')
