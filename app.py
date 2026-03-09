from flask import Flask, render_template, request, redirect, url_for, session
from db.database import Database
from models.usuario import UsuarioModel

app = Flask(__name__)
app.secret_key = 'pipetapp_secret_key_2026'
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
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        usuario_encontrado = modelo_usuario.login(email, password)
        if usuario_encontrado:
            session['user_id'] = usuario_encontrado['id']
            session['username'] = usuario_encontrado['username']
            return redirect(url_for('dashboard'))
        else:
            return 'Email o cntraseña no econtrada'
    return render_template('login.html')    
@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return f"<h1>Hola {session['username']}, bienvenido a tu Dashboard de PipetApp 🐾</h1>"
    return redirect(url_for('login'))



   
if __name__ == '__main__':
    app.run(debug=True)
    