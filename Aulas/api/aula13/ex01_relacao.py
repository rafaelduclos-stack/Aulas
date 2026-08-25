import sqlite3

conexao = sqlite3.connect("biblioteca.db")

conexao.execute("""
create table if not exists autores (
    id integer primary key autoincrement,
    nome text
)
""")

conexao.execute("""
create table if not exists livros (
    id integer primary key autoincrement,
    titulo text,
    autor_id integer,
    foreign key (autor_id) references autores(id)
)
""")

conexao.execute(
    "insert into autores (nome) values (?)",
    ("Machado de Assis",)
)

conexao.execute(
    "insert into autores (nome) values (?)",
    ("Jose de Alencar",)
)

conexao.execute(
    "insert into livros (titulo, autor_id) values (?, ?)",
    ("Dom Casmurro", 1)
)

conexao.execute(
    "insert into livros (titulo, autor_id) values (?, ?)",
    ("Memorias Postumas de Bras Cubas", 1)
)

conexao.execute(
    "insert into livros (titulo, autor_id) values (?, ?)",
    ("O Guarani", 2)
)

conexao.commit()
conexao.close()