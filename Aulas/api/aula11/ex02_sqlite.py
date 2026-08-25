import sqlite3

conexao = sqlite3.connect("loja.db")

cursor = conexao.execute("select * from produtos")

produtos = cursor.fetchall()

for produto in produtos:
    print(produto)

conexao.close()