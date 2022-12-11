import tkinter as tk


def make_nav_button(parent, controller, F, text, frame=None, **kwargs):
    nav_button = tk.Button(parent, text=text,
    command=lambda : controller.show_frame(F, frame, **kwargs))
    return nav_button

    
def make_header(parent, text):
    header = tk.Label(parent, text=text, font='Helvetica 28 bold')
    header.grid(row=1, column=0, sticky='w', columnspan=parent.grid_size()[1]+1)
        
        
def make_entry(parent, text, row):
    entry_label = tk.Label(parent, text=text, font='Helvetica 16')
    entry_label.grid(row=row, column=0, sticky='w')
    entry = tk.Entry(parent)
    entry.grid(row=row, column=1, sticky='w')
    return entry
