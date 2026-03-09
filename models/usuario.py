from db.database import Database
from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self, nombre, email, password):
        conexion = self.db.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                password_encriptada = generate_password_hash(password)
                sql = "INSERT INTO usuarios (username, email, password_hash) VALUES (%s, %s, %s)"
                valores = (nombre, email, password_encriptada)
                cursor.execute(sql, valores)
                conexion.commit()
                return True
            except Exception as e:
                print(f"Error en el modelo usuario: {e}")
                return False
            finally:
                if 'cursor' in locals():
                    cursor.close()
                conexion.close()
        return False


