from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/produtos")
def produtos():
    produtos = [
        {"id":1,"nome":"Vassoura","preco":20.0,"disponivel":True},
        {"id":2,"nome":"Bomba nuclear","preco":90000000000000,"disponivel":True},
        {"id":3,"nome":"Chiclete","preco":2,"disponivel":False}
    ]
    return jsonify(produtos)

if __name__ == "__main__":
    app.run(debug=True)