from flask import Flask
app = Flask(__name__)
@app.route("/")
def inicio():
    return "Bem vindo!"
@app.route("/curso")
def sobre():
    return "Curso: Desenvolvimento de sistemas"
@app.route("/escola")
def aluno():
    return "Escola: Pedro Boaretto Neto"
if __name__ == "__main__":
    app.run(debug=True)