from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = []

@app.route("/tarefas", methods=["GET"])
def listar():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar():
    novo = request.get_json()
    if "titulo" not in novo:
        return jsonify({"erro": "O campo titulo e obrigatorio"}), 400
    tarefas.append(novo)
    return jsonify(novo), 201

if __name__ == ("__main__"):
    app.run(debug=True)