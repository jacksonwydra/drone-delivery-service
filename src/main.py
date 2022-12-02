from rse import RSEConnection
from tkwrapper import TKWrapper

def main():
    db = RSEConnection()
    tk = TKWrapper('Drone Delivery Service')
    
    a_names = db.get_a_names()
    tk.make_table(a_names)
    
    tk.run()
    db.disconnect()
    

if __name__ == '__main__':
    main()
