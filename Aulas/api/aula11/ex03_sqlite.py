from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def conectar():
    conexao = sqlite3.connect("loja.db")
    conexao.row_factory = sqlite3.Row
    return conexao


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    conexao = conectar()

    cursor = conexao.execute("select * from produtos")
    produtos = cursor.fetchall()

    conexao.close()

    return jsonify([dict(produto) for produto in produtos])


@app.route("/produtos", methods=["POST"])
def adicionar_produto():
    dados = request.get_json()

    if "preco" not in dados:
        return jsonify({"erro": "O preço e obrigatorio"}), 400

    conexao = conectar()

    conexao.execute(
        "insert into produtos (nome, preco) values (?, ?)",
        (dados["nome"], dados["preco"])
    )

    conexao.commit()
    conexao.close()

    return jsonify({"mensagem": "Produto adicionado"}), 201

if __name__ == "__main__":
    app.run(debug=True)