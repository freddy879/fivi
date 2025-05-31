from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar Flask-CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# Lista para almacenar pedidos
pedidos = []

@app.route('/pedido', methods=['POST'])
def recibir_pedido():
    data = request.json
    direccion = data.get("direccion")
    telefono = data.get("telefono")
    carrito = data.get("carrito")

    if not direccion or not telefono or not carrito:
        return jsonify({"error": "Faltan datos en el pedido"}), 400

    pedido = {"direccion": direccion, "telefono": telefono, "carrito": carrito}
    pedidos.append(pedido)
    return jsonify({"mensaje": "Pedido recibido correctamente", "pedido": pedido})

@app.route('/pedidos', methods=['GET'])
def obtener_pedidos():
    return jsonify(pedidos)

if __name__ == '__main__':
    app.run(debug=True)
