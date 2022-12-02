import tkinter as tk
import rse

def main():
    cnx = rse.get_rse_connection()
    cursor = cnx.cursor()
    
    query = ('''SELECT
                    username,
                    first_name,
                    last_name
                FROM users
                WHERE first_name LIKE %s''')
    a_names = 'A%'
    cursor.execute(query, (a_names, ))
    
    for username, first_name, last_name in cursor:
        print(f'{first_name} {last_name} ({username})')
    
    cnx.close()

if __name__ == '__main__':
    main()
