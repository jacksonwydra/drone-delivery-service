import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


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


def make_date(parent, text, row):
    date_label = tk.Label(parent, text=text, font='Helvetica 16')
    date_label.grid(row=row, column=0, sticky='w')
    date_entry = DateEntry(parent, selectmode='day', day=1, month=1, year=2000)
    date_entry.grid(row=row, column=1, sticky='w')
    
    return date_entry
