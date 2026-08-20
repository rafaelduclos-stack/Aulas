from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {"id": 1,"nome": "Refri","preco": 5.00},
    {"id": 2,"nome": "Pizza","preco": 90.00},
    {"id": 3,"nome": "Hámburguer","preco": 45.00}
]

@app.route("/produtos", methods=["GET"])
def listar():
    return jsonify(produtos)

@app.route("/produtos", methods=["POST"])
def criar():
    novo = request.get_json()
    produtos.append(novo)
    return jsonify(novo), 201

if __name__ == ("__main__"):
    app.run(debug=True)