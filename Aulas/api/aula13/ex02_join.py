from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


def conectar():
    conexao = sqlite3.connect("biblioteca.db")
    conexao.row_factory = sqlite3.Row
    return conexao


@app.route("/livros-completo", methods=["GET"])
def livros_completo():
    conexao = conectar()

    cursor = conexao.execute("""
        select livros.id, livros.titulo, autores.nome as autor
        from livros
        join autores on livros.autor_id = autores.id
    """)

    livros = cursor.fetchall()

    conexao.close()

    return jsonify([dict(livro) for livro in livros])

if __name__ == "__main__":
    app.run(debug=True)