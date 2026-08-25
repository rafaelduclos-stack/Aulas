from flask import Flask
from datetime import date

hoje = date.today()

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bem vindo(a)"

@app.route("/saudacao")
def dia():
    return str(hoje)

if __name__ == "__main__":
    app.run(debug=True)