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
    'get_warnings': True,
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
    
    try:
        cursor.execute(query, params)
    except Exception as e:
        print(e)
        return e

    cnx.commit()
    warnings = cursor.fetchwarnings()
    if warnings: print(warnings)
    cnx.close()

    if cursor.rowcount == 0:
        return 'No rows affected'

    return None


def get_view(query):
    cnx = rse_connect()
    cursor = cnx.cursor()
    cursor.execute(query)
    output = cursor.fetchall()
    output.insert(0, cursor.column_names)
    warnings = cursor.fetchwarnings()
    if warnings: print(warnings)
    cnx.close()
    
    return output


def add_owner(params):
    '''[1] add_owner

    Args:
        params (tuple): (username, first_name, last_name, address, birthdate)
    '''
    # Check for null values
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call add_owner(%s, %s, %s, %s, %s);'
    return execute_procedure(query, params)
    

def add_employee(params):
    '''[2] add_employee

    Args:
        params (tuple): (username, first_name, last_name, address, birthdate, taxID, hired, experience, salary)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call add_employee(%s, %s, %s, %s, %s, %s, %s, %s, %s);'
    return execute_procedure(query, params)
    
    
def add_pilot_role(params):
    '''[3] add_pilot_role

    Args:
        params (tuple): (username, licenseID, pilot_experience)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call add_pilot_role(%s, %s, %s);'
    return execute_procedure(query, params)
    
    
def add_worker_role(params):
    '''[4] add_worker_role

    Args:
        params (tuple): (username)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call add_worker_role(%s);'
    return execute_procedure(query, params)
    
    
def add_ingredient(params):
    '''[5] add_ingredient

    Args:
        params (tuple): (barcode, iname, weight)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call add_ingredient(%s, %s, %s);'
    return execute_procedure(query, params)
    
    
def add_drone(params):
    '''[6] add_drone

    Args:
        params (tuple): (id, tag, fuel, capacity, sales, flown_by)
    '''
    if not all(params[:-1]): return 'Make sure to fill out all values.'
    query = 'call add_drone(%s, %s, %s, %s, %s, %s);'
    return execute_procedure(query, params)
    
    
def add_restaurant(params):
    '''[7] add_restaurant

    Args:
        params (tuple): (long_name, rating, spent, location)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call add_restaurant(%s, %s, %s, %s);'
    return execute_procedure(query, params)
    
    
def add_service(params):
    '''[8] add_service

    Args:
        params (tuple): (id, long_name, home_base, manager)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call add_service(%s, %s, %s, %s);'
    return execute_procedure(query, params)
    
    
def add_location(params):
    '''[9] add_location

    Args:
        params (tuple): (label, x_coord, y_coord, space)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call add_location(%s, %s, %s, %s);'
    return execute_procedure(query, params)


def start_funding(params):
    '''[10] start_funding

    Args:
        params (tuple): (owner, long_name)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call start_funding(%s, %s);'
    return execute_procedure(query, params)


def hire_employee(params):
    '''[11] hire_employee

    Args:
        params (tuple): (username, id)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call hire_employee(%s, %s);'
    return execute_procedure(query, params)


def fire_employee(params):
    '''[12] fire_employee

    Args:
        params (tuple): (username, id)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call fire_employee(%s, %s);'
    return execute_procedure(query, params)


def manage_service(params):
    '''[13] manage_service

    Args:
        params (tuple): (username, id)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call manage_service(%s, %s);'
    return execute_procedure(query, params)


def takeover_drone(params):
    '''[14] takeover_drone

    Args:
        params (tuple): (username, id, tag)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call takeover_drone(%s, %s, %s);'
    return execute_procedure(query, params)


def join_swarm(params):
    '''[15] join_swarm

    Args:
        params (tuple): (id, tag, swarm_leader_tag)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call join_swarm(%s, %s, %s);'
    return execute_procedure(query, params)


def leave_swarm(params):
    '''[16] leave_swarm

    Args:
        params (tuple): (id, tag)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call leave_swarm(%s, %s);'
    return execute_procedure(query, params)


def load_drone(params):
    '''[17] load_drone

    Args:
        params (tuple): (id, tag, barcode, more_packages, price)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call load_drone(%s, %s, %s, %s, %s);'
    return execute_procedure(query, params)


def refuel_drone(params):
    '''[18] refuel_drone

    Args:
        params (tuple): (id, tag, more_fuel)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call refuel_drone(%s, %s, %s);'
    return execute_procedure(query, params)


def fly_drone(params):
    '''[19] fly_drone

    Args:
        params (tuple): (id, tag, destination)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call fly_drone(%s, %s, %s);'
    return execute_procedure(query, params)


def purchase_ingredient(params):
    '''[20] purchase_ingredient

    Args:
        params (tuple): (long_name, id, tag, barcode, quantity)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call purchase_ingredient(%s, %s, %s, %s, %s);'
    return execute_procedure(query, params)


def remove_ingredient(params):
    '''[21] remove_ingredient

    Args:
        params (tuple): (barcode,)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call remove_ingredient(%s);'
    return execute_procedure(query, params)


def remove_drone(params):
    '''[22] remove_drone

    Args:
        params (tuple): (id, tag)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call remove_drone(%s, %s);'
    return execute_procedure(query, params)


def remove_pilot_role(params):
    '''[23] remove_pilot_role

    Args:
        params (tuple): (username,)
    '''
    if not all(params): return 'Make sure to fill out all values.'
    query = 'call remove_pilot_role(%s);'
    return execute_procedure(query, params)
    
    
def display_owner_view():
    '''
    [24] display_owner_view
    '''
    query = 'select * from display_owner_view;'
    owner_view = get_view(query)
    
    return owner_view
    

def display_employee_view():
    '''
    [25] display_employee_view
    '''
    query = 'select * from display_employee_view;'
    employee_view = get_view(query)
    
    return employee_view


def display_pilot_view():
    '''
    [26] display_pilot_view
    '''
    query = 'select * from display_pilot_view;'
    pilot_view = get_view(query)
    
    return pilot_view


def display_location_view():
    '''
    [27] display_location_view
    '''
    query = 'select * from display_location_view;'
    location_view = get_view(query)
    
    return location_view


def display_ingredient_view():
    '''
    [28] display_ingredient_view
    '''
    query = 'select * from display_ingredient_view;'
    ingredient_view = get_view(query)
    
    return ingredient_view


def display_service_view():
    '''
    [29] display_service_view
    '''
    query = 'select * from display_service_view;'
    service_view = get_view(query)
    
    return service_view


def display_drone_view():
    '''
    display_drone_view
    '''
    query = 'select * from drones;'
    drone_view = get_view(query)
    
    return drone_view


def display_worker_view():
    '''
    display_worker_view
    '''
    query = 'select * from workers;'
    worker_view = get_view(query)
    
    return worker_view


def display_restaurant_view():
    '''
    display_restaurant_view
    '''
    query = 'select * from restaurants;'
    restaurant_view = get_view(query)
    
    return restaurant_view


def display_payload_view():
    '''
    display_payload_view
    '''
    query = 'select * from payload;'
    payload_view = get_view(query)
    
    return payload_view
