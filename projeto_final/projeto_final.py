from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


def conectar():
    conexao = sqlite3.connect("confeitariaferduclos.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabelas():
    conexao = conectar()
    conexao.execute("""
        create table if not exists produtos (
            id integer primary key autoincrement,
            nome varchar(75) not null,
            preco decimal(10,2) not null,
            quantidade int,
            categoria varchar(50)
        )
    """)
    conexao.execute("""
        create table if not exists bolos (
            id integer primary key autoincrement,
            nome varchar(50) not null,
            sabor varchar(50) not null,
            tamanho varchar(20) not null,
            produto_id integer not null,
            foreign key (produto_id) references produtos(id)
        )
    """)
    conexao.commit()
    conexao.close()


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    conexao = conectar()
    cursor = conexao.execute("select * from produtos")
    produtos = [dict(l) for l in cursor.fetchall()]
    conexao.close()
    return jsonify(produtos)


@app.route("/produtos/<int:id>", methods=["GET"])
def obter_produto(id):
    conexao = conectar()
    linha = conexao.execute("select * from produtos where id = ?", (id,)).fetchone()
    conexao.close()
    if linha is None:
        return jsonify({"erro": "Produto não encontrado"}), 404
    return jsonify(dict(linha))


@app.route("/produtos", methods=["POST"])
def criar_produto():
    novo = request.get_json()
    if "nome" not in novo or "preco" not in novo:
        return jsonify({"erro": "Nome e preco sao obrigatorios"}), 400
    conexao = conectar()
    cursor = conexao.execute(
        "insert into produtos (nome, preco, categoria, quantidade) values (?, ?, ?, ?)",
        (novo["nome"], novo["preco"], novo["categoria"], novo["quantidade"])
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return jsonify({"id": novo_id, "nome": novo["nome"], "preco": novo["preco"], "categoria": novo["categoria"], "quantidade": novo["quantidade"]}), 201


@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    dados = request.get_json()
    if "nome" not in dados or "preco" not in dados:
        return jsonify({"erro": "Nome e preco sao obrigatorios"}), 400
    conexao = conectar()
    cursor = conexao.execute(
        "update produtos set nome = ?, preco = ?, categoria = ?, quantidade = ? where id = ?",
        (dados["nome"], dados["preco"], dados["categoria"], dados["quantidade"], id)
    )
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()
    if afetadas == 0:
        return jsonify({"erro": "Produto nao encontrado"}), 404
    return jsonify({"id": id, "nome": dados["nome"], "preco": dados["preco"], "categoria": dados["categoria"], "quantidade": dados["quantidade"]})


@app.route("/produtos/<int:id>", methods=["DELETE"])
def apagar_produto(id):
    conexao = conectar()
    cursor = conexao.execute("delete from produtos where id = ?", (id,))
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()
    if afetadas == 0:
        return jsonify({"erro": "Produto nao encontrado"}), 404
    return jsonify({"mensagem": "Produto apagado com sucesso"})


@app.route("/bolos", methods=["GET"])
def listar_bolos():
    conexao = conectar()
    cursor = conexao.execute("select * from bolos")
    bolos = [dict(l) for l in cursor.fetchall()]
    conexao.close()
    return jsonify(bolos)


@app.route("/bolos/<int:id>", methods=["GET"])
def obter_bolo(id):
    conexao = conectar()
    linha = conexao.execute("""
        select bolos.id, bolos.nome, bolos.sabor, bolos.tamanho, bolos.produto_id, produtos.nome as produto_nome from bolos
        join produtos on bolos.produto_id = produtos.id where bolos.id = ?
    """, (id,)).fetchone()
    conexao.close()
    if linha is None:
        return jsonify({"erro": "Bolo nao encontrado"}), 404
    return jsonify(dict(linha))


@app.route("/bolos", methods=["POST"])
def criar_bolo():
    novo = request.get_json()
    if not novo or "nome" not in novo or "sabor" not in novo or "tamanho" not in novo or "produto_id" not in novo:
        return jsonify({"erro": "Nome, sabor, tamanho e produto_id sao obrigatórios"}), 400
    conexao = conectar()
    produto = conexao.execute("select id from produtos where id = ?", (novo["produto_id"],)).fetchone()
    if produto is None:
        conexao.close()
        return jsonify({"erro": "Produto_id informado nao existe"}), 400
    cursor = conexao.execute(
        "insert into bolos (nome, sabor, tamanho, produto_id) values (?, ?, ?, ?)",
        (novo["nome"], novo["sabor"], novo["tamanho"], novo["produto_id"])
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return jsonify({"id": novo_id, **novo}), 201


@app.route("/bolos/<int:id>", methods=["PUT"])
def atualizar_bolo(id):
    dados = request.get_json()
    if not dados or "nome" not in dados or "sabor" not in dados or "tamanho" not in dados or "produto_id" not in dados:
        return jsonify({"erro": "nome, sabor, preco e produto_id sao obrigatorios"}), 400
    conexao = conectar()
    produto = conexao.execute("select id from produtos where id = ?", (dados["produto_id"],)).fetchone()
    if produto is None:
        conexao.close()
        return jsonify({"erro": "produto_id informado nao existe"}), 400
    cursor = conexao.execute(
        "update bolos set nome = ?, sabor = ?, tamanho = ?, produto_id = ? where id = ?",
        (dados["nome"], dados["sabor"], dados["tamanho"], dados["produto_id"], id)
    )
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()
    if afetadas == 0:
        return jsonify({"erro": "Bolo nao encontrado"}), 404
    return jsonify({"id": id, **dados})


@app.route("/bolos/<int:id>", methods=["DELETE"])
def apagar_bolo(id):
    conexao = conectar()
    cursor = conexao.execute("delete from bolos where id = ?", (id,))
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()
    if afetadas == 0:
        return jsonify({"erro": "Bolo não encontrado"}), 404
    return jsonify({"mensagem": "Bolo apagado com sucesso"})


@app.route("/produtos/<int:id>/bolos", methods=["GET"])
def bolos_do_produto(id):
    conexao = conectar()
    produto = conexao.execute("select id from produtos where id = ?", (id,)).fetchone()
    if produto is None:
        conexao.close()
        return jsonify({"erro": "Produto não encontrado"}), 404
    cursor = conexao.execute("select * from bolos where produto_id = ?", (id,))
    bolos = [dict(l) for l in cursor.fetchall()]
    conexao.close()
    return jsonify(bolos)


@app.route("/bolos/busca", methods=["GET"])
def buscar_bolos():
    nome = request.args.get("nome", "")
    conexao = conectar()
    cursor = conexao.execute("select * from bolos where nome like ?", (f"%{nome}%",))
    bolos = [dict(l) for l in cursor.fetchall()]
    conexao.close()
    return jsonify(bolos)


if __name__ == "__main__":
    criar_tabelas()
    app.run(debug=True)