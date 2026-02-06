from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Base de datos estática
USERS_DATABASE = {
    "admin": "12345",
    "juan": "pancito123",
    "maria": "claveSegura77"
}

@app.route('/')
def home():
    return "API de Validación activa. Usa el endpoint /login", 200

@app.route('/login', methods=['GET'])
def login():
    user_input = request.args.get('user')
    pass_input = request.args.get('pass')

    if not user_input or not pass_input:
        return jsonify({"status": "error", "message": "Faltan parámetros"}), 400

    if user_input in USERS_DATABASE and USERS_DATABASE[user_input] == pass_input:
        return jsonify({
            "status": "success", 
            "message": f"Bienvenido, {user_input}."
        }), 200
    else:
        return jsonify({
            "status": "error", 
            "message": "Credenciales inválidas"
        }), 401

if __name__ == '__main__':
    # Render asigna un puerto dinámico mediante la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)