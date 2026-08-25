from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def conectar():
    conexao = sqlite3.connect("biblioteca.db")
    conexao.row_factory = sqlite3.Row
    return conexao


@app.route("/autores/<int:autor_id>/livros", methods=["GET"])
def livros_autor(autor_id):
    conexao = conectar()

    cursor = conexao.execute(
        "select * from livros where autor_id = ?",
        (autor_id,)
    )

    livros = cursor.fetchall()

    conexao.close()

    return jsonify([dict(livro) for livro in livros])


@app.route("/livros/busca", methods=["GET"])
def buscar_livros():
    titulo = request.args.get("titulo", "")

    conexao = conectar()

    cursor = conexao.execute(
        "select * from livros where titulo like ?",
        (f"%{titulo}%",)
    )

    livros = cursor.fetchall()

    conexao.close()

    return jsonify([dict(livro) for livro in livros])

if __name__ == "__main__":
    app.run(debug=True)