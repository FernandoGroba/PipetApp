from flask import Flask, render_template, request, redirect, url_for
from db.database import Database
from models.usuario import UsuarioModel

app = Flask(__name__)
db = Database()
modelo_usuario = UsuarioModel()

@app.route('/')
def inicio():
    return redirect(url_for('registro'))



@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')

        if modelo_usuario.registrar(nombre, email, password):
            return redirect(url_for('login'))
        else:
            return "Hubo un error al guardar el usuario en la base de datos."
    return render_template ('registro.html')

@app.route('/login')
def login():
    # Por ahora solo un mensaje para probar que el redirect funciona
    return "<h1>¡Registro exitoso! Ahora estás en el Login (Próximamente)</h1>"

   
if __name__ == '__main__':
    app.run(debug=True)
    