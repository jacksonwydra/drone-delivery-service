import sys
sys.path.insert(0, "./")

from src.tkwrapper import TKWrapper

def main():
    root = TKWrapper(title='Drone Delivery Service')
    root.mainloop()
    

if __name__ == '__main__':
    main()
