from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/produto")
def produto():
    produto = {
        "id" : 1,
        "nome" : "Refrigerante",
        "preco" : 5.00,
        "disponivel" : True
    }
    return jsonify(produto)

if __name__ == "__main__":
    app.run(debug=True)