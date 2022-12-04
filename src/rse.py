import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv


def rse_connect():
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
        
    return cnx


def execute_query(query, params=None):
    cnx = rse_connect()
    cursor = cnx.cursor()
    cursor.execute(query, params)
    output = cursor.fetchall()
    output.insert(0, cursor.column_names)
    cnx.close()
    
    return output


def display_employee_view():
    query = ('SELECT * FROM display_employee_view')
    employee_view = execute_query(query)
    
    return employee_view
