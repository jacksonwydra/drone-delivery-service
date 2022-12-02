import tkinter as tk

class TKWrapper:
    def __init__(self, title='', width=400, height=300):
        self.root = tk.Tk()
        self.title = title
        self.width = width
        self.height = height
        self.setup_root()
    
    
    def setup_root(self) -> None:
        self.root.title(self.title)
        
        # Center the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 2
        self.root.geometry(f'{self.width}x{self.height}+{x}+{y}')
        
        
    def run(self) -> None:
        self.root.mainloop()
    
    
    def make_table(self, data:list[tuple]) -> None:
        table = tk.Frame(self.root,relief=tk.SOLID, borderwidth=1)
        for i, entry in enumerate(data):
            table.columnconfigure(i, weight=1)
            for j, value in enumerate(entry):
                font = ('Helvetica', 14, 'bold' if i == 0 else '')
                frame = tk.Frame(table, relief=tk.SOLID, borderwidth=1)
                frame.grid(row=i, column=j, sticky='nsew')
                label = tk.Label(frame, text=value, font=font)
                label.pack(padx=5, pady=5)
        table.pack(padx=5, pady=5, fill=tk.X)