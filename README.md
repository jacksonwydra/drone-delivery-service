# drone-delivery-service

This project is a python GUI application for phase 4 of CS 4400.
It uses tkinter for the GUI elements and mysql for the connection with the restaurant_supply_express databse.

## Project Members

- Jackson Wydra
- Regina Munoz
- Taylor Hunter

## Set Up Project

1. Create and activate a virtual environment:

    ```cmd
    python -m venv venv
    ```

    Mac:

    ```cmd
    source venv/bin/activate
    ```

    Windows:

    ```cmd
    venv/Scripts/activate
    ```

2. Install required packages:

    ```cmd
    python -m pip install -r requirements.txt
    ```

3. Create a '.env' file with your MySQL database username and password:

    .env

    ```bash
    RSE_USERNAME=username
    RSE_PASSWORD=password
    ```

4. Run the 'main.py' file in the 'src' directory:

    ```cmd
    python src/main.py
    ```
