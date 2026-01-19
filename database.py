import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'fernando',
            'database': 'pipetapp'
        }

    def conectar(self):
        try:
            return mysql.connector.connect(**self.config)
        except Error as e:
            print(f'Error al conectar: {e}')

    def guardar_mascota(self, mascota_obj):
        conexion = self.conectar()
        if conexion:
            cursor = conexion.cursor()
            sql = "INSERT INTO mascotas (nombre, especie, peso, ultima_pipeta) VALUES (%s, %s, %s, %s)"
            valores = (mascota_obj.nombre, mascota_obj.especie,
                       mascota_obj.peso, mascota_obj.ultima_pipeta)
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
