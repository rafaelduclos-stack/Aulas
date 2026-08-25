from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id":1,"nome":"Vassoura","preco":20.0,"disponivel":True},
    {"id":2,"nome":"Bomba nuclear","preco":90000000000000,"disponivel":True},
    {"id":3,"nome":"Chiclete","preco":2,"disponivel":False}
]

@app.route("/produtos")
def produto():
    return jsonify(produtos)


@app.route("/produtos/<int:id>")
def procurar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)
        
    return jsonify({"erro":"Produto nao encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)