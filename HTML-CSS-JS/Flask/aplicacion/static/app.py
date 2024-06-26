
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

estudiantes = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method =="GET":
        return render_template("login.html")
    else:
        name = request.form.get("nombre")
        print(name)
        return render_template("saludo.html", name = name)

@app.route("/info", methods = ["GET", "POST"])
def info():
    if request.method == "GET":
        return render_template("info.html")

    else:
        nombre = request.form.get("nombre")
        carrera = request.form.get("carrera")
        estudiante = {"nombre": nombre, "carrera": carrera}
        estudiantes.append(estudiante)
        print(estudiante)
        return render_template("tabla.html", estudiantes = estudiantes