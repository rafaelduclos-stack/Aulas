from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def conectar():
    conexao = sqlite3.connect("tarefas.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar()

    conexao.execute("""
        create table if not exists tarefas (
            id integer primary key autoincrement,
            titulo text,
            feita integer
        )
    """)

    conexao.commit()
    conexao.close()


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    conexao = conectar()

    cursor = conexao.execute("select * from tarefas")
    tarefas = cursor.fetchall()

    conexao.close()

    return jsonify([dict(tarefa) for tarefa in tarefas])


@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    dados = request.get_json()

    conexao = conectar()

    conexao.execute(
        "insert into tarefas (titulo, feita) values (?, ?)",
        (dados["titulo"], dados["feita"])
    )

    conexao.commit()
    conexao.close()

    return jsonify({"mensagem": "Tarefa adicionada"}), 201


@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    dados = request.get_json()

    conexao = conectar()

    tarefa = conexao.execute(
        "select * from tarefas where id = ?",
        (id,)
    ).fetchone()

    if tarefa is None:
        conexao.close()
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    conexao.execute(
        "update tarefas set titulo = ?, feita = ? where id = ?",
        (dados["titulo"], dados["feita"], id)
    )

    conexao.commit()
    conexao.close()

    return jsonify({"mensagem": "Tarefa atualizada"})


@app.route("/tarefas/<int:id>", methods=["DELETE"])
def apagar_tarefa(id):
    conexao = conectar()

    tarefa = conexao.execute(
        "select * from tarefas where id = ?",
        (id,)
    ).fetchone()

    if tarefa is None:
        conexao.close()
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    conexao.execute(
        "delete from tarefas where id = ?",
        (id,)
    )

    conexao.commit()
    conexao.close()

    return jsonify({"mensagem": "Tarefa apagada"})

if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)