import tkinter as tk
from rse import RSEConnection

def main():
    db = RSEConnection()
    db.connect()
    
    db.print_a_names()
    
    db.disconnect()

if __name__ == '__main__':
    main()
