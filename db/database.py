import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.config = {
            'host':'localhost',
            'port': 3307,
            'user':'root',
            'password':'',
            'database':'pipetapp',

        }

    def conectar(self):

        try:
            return mysql.connector.connect(**self.config)
        except Error as e:
            print(f"DEBUG: Error de conexión -> {e}") 
            return None



