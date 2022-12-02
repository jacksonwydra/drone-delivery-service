import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

class RSEConnection:
    def __init__(self, cnx=None):
        self.cnx = cnx
        
    
    def connect(self) -> None:
        load_dotenv()
        RSE_USERNAME = os.environ.get("RSE_USERNAME")
        RSE_PASSWORD = os.environ.get("RSE_PASSWORD")

        config = {
        'user': RSE_USERNAME,
        'password': RSE_PASSWORD,
        'host': '127.0.0.1',
        'database': 'restaurant_supply_express',
        'raise_on_warnings': True
        }

        try:
            cnx = mysql.connector.connect(**config)
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Username or password are incorrect")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database not found")
            else:
                print(e)
            cnx = None
            
        self.cnx = cnx
        
        
    def disconnect(self) -> None:
        self.cnx.close()
        
        
    def print_a_names(self):
        cursor = self.cnx.cursor()
    
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
        