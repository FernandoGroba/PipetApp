from flask import Flask
from db.database import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def inicio():
    try:
        conexion = db.conectar()
        if conexion:
            conexion.close()
            return "<h1>¡CONECTADO AL 3307! ✅</h1>"
        else:
            return "<h1>Error: db.conectar() devolvió None ❌</h1>"
    except Exception as e:
        # Esto nos va a mostrar el error técnico real de MySQL en el navegador
        return f"<h1>Error Técnico: {str(e)} ❌</h1>"

if __name__ == '__main__':
    app.run(debug=True)
    