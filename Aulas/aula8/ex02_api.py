from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bem vindo(a)"

@app.route("/curso")
def curso():
    return "Desenvolvimento de Sistemas"

@app.route("/escola")
def escola():
    return "CEEP Pedro Boaretto Neto"

if __name__ == "__main__":
    app.run(debug=True)