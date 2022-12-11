import tkinter as tk
from src.utils import make_home_button, make_header


class DisplayViewFrame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        
        nav = tk.Frame(self)
        home_button = make_home_button(nav, controller, self)
        home_button.grid(row=0, column=0, sticky='w')
        
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