from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id":1,"nome":"Vassoura","preco":20.0,"disponivel":True},
    {"id":2,"nome":"Bomba nuclear","preco":90000000000000,"disponivel":True},
    {"id":3,"nome":"Chiclete","preco":2,"disponivel":False}
]

#listar tudo
@app.route("/produtos")
def produto():
    return jsonify(produtos)

#listar por id
@app.route("/produtos/<int:id>")
def listar_id(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)
        
    return jsonify({"erro":"Produto nao encontrado"}), 404

#listar disponivies
@app.route("/produtos/disponiveis")

def listar_disponiveis():
    disponiveis = []
    for produto in produtos:
        if produto["disponivel"] == True:
            disponiveis.append(produto)
    return jsonify(disponiveis)

if __name__ == "__main__":
    app.run(debug=True)
