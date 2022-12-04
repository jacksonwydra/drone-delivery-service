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


def execute_procedure(query, params=None):
    cnx = rse_connect()
    cursor = cnx.cursor()
    cursor.execute(query, params)
    cnx.commit()
    cnx.close()


def get_view(query):
    cnx = rse_connect()
    cursor = cnx.cursor()
    cursor.execute(query)
    output = cursor.fetchall()
    output.insert(0, cursor.column_names)
    cnx.close()
    
    return output


def add_employee(params):
    '''[2] add_employee

    Args:
        params (tuple): (username, first_name, last_name, address, birthdate, taxID, hired, experience, salary)
    '''
    query = 'call add_employee(%s, %s, %s, %s, %s, %s, %s, %s, %s);'
    execute_procedure(query, params)
    

def display_employee_view():
    '''[25] display_employee_view

    Returns:
        list(tuple): Rows of the view with headers
    '''
    query = 'select * from display_employee_view;'
    employee_view = get_view(query)
    
    return employee_view
