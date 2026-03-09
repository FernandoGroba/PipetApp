from db.database import Database

class MascotaModel:
    def __init__(self):
        self.db = Database()

    def obtener_por_usuario(self, usuario_id):
        conexion = self.db.conectar()
        if conexion:
            try:
                cursor = conexion.cursor(dictionary=True)
                sql = "SELECT id, nombre, raza, peso, ultima_pipeta FROM mascotas WHERE usuario_id = %s"
                cursor.execute(sql, (usuario_id,))
                return cursor.fetchall()
            except Exception as e:
                print (f'Error al obtener mascotas {e}')
                return[]
            finally:
                if conexion:
                    cursor.close()
                    conexion.close()
        return False  

    def registrar(self, usuario_id, nombre, especie, raza, peso, ultima_pipeta ):
        conexion = self.db.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                sql = "INSERT INTO mascotas(usuario_id, nombre, raza, peso, ultima_pipeta) VALUES (%s, %s, %s, %s, %s)"
                valores = (usuario_id, nombre, raza, peso, ultima_pipeta)
                cursor.execute(sql, valores)
                conexion.commit()
                return True
            except Exception as e:
                print(f'Error al registrar: {e}')
                return False
            finally:
                cursor.close()
                conexion.close()
        return False


                   