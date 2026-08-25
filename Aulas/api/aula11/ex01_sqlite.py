import sqlite3

conexao = sqlite3.connect("loja.db")

conexao.execute("""
create table if not exists produtos (
    id integer primary key autoincrement,
    nome text,
    preco real
)
""")

conexao.execute("insert into produtos (nome, preco) values (?, ?)", ("Arroz", 25.50))
conexao.execute("insert into produtos (nome, preco) values (?, ?)", ("Feijao", 8.90))
conexao.execute("insert into produtos (nome, preco) values (?, ?)", ("Macarrao", 5.50))

conexao.commit()
conexao.close()