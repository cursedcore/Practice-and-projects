import os
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    table = db.execute("SELECT * FROM exchanges WHERE id=?",
                       session["user_id"])
    remaining_cash = db.execute(
        "SELECT cash FROM users WHERE id=?", session["user_id"])

    float_total = 0.0
    total = str()
    for i in table:
        total = i["total"]
        if len(total) > 1:
            total = total.lstrip("$")
            total = total.replace(",", "")
            float_total += float(total)

    return render_template("index.html", table=table, total=float_total, cash=remaining_cash[0]["cash"])


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():


    if request.method == "GET":
        return render_template("buy.html")


    quote = lookup(request.form.get("symbol"))

    if quote is None:
        return apology("No se encontró la acción", 400)

    shares = request.form.get("shares")

    try:
        shares = int(shares)
    except:
        return apology("Debes escribir un numero entero de acciones", 400)

    if not shares or shares <= 0:
        return apology("Por favor escriba el numero de acciones", 400)

    user = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
    current_cash = user[0]["cash"]

    total = quote["price"] * float(shares)
    if total > current_cash:
        return apology("No tienes dinero suficiente", 400)

    current_cash -= total

    db.execute("INSERT INTO history (id, symbol, shares, price) VALUES(?,?,?,?)",
               session["user_id"],
               quote["symbol"],
               shares,
               usd(quote["price"])
               )

    db.execute("UPDATE users SET cash=? WHERE id=?",
               current_cash, session["user_id"])


    user_shares = db.execute(
        "SELECT * FROM exchanges WHERE symbol=? AND id=?", quote["symbol"], session["user_id"])


    if not user_shares:
        db.execute("INSERT INTO exchanges VALUES(?,?,?,?,?,?)",
                   session["user_id"],
                   quote["symbol"],
                   quote["name"],
                   shares,
                   usd(quote["price"]),
                   usd(total))

    else:
        total_shares = user_shares[0]["shares"] + float(shares)
        db.execute("UPDATE exchanges SET shares=? WHERE id=? AND symbol =?",
                   total_shares, session["user_id"], quote["symbol"])
    flash("Bought!")

    return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history = db.execute(
        "SELECT * FROM history WHERE id=?", session["user_id"])
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("Debes escribir un nombre de usuario", 403)


        elif not request.form.get("password"):
            return apology("Debes escribir una contraseña", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Nombre de usuario o contraseña inválidos", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    session.clear()
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "GET":
        return render_template("quote.html")

    symbol = lookup(request.form.get("symbol"))
    if symbol is None:
        return apology("No se encontró la acción", 400)
    return render_template("quoted.html", value=symbol)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if not request.form.get("username"):
        return apology("Debes escribir un nombre de usuario", 400)

    if not request.form.get("password"):
        return apology("Debes escribir una contraseña", 400)

    if request.form.get("password") != request.form.get("confirmation"):
        return apology("Las contraseñas no coinciden", 400)

    rows = db.execute("SELECT * FROM users WHERE username=?",
                      request.form.get("username"))

    if len(rows) == 1:
        return apology("Ese nombre de usuario ya existe", 400)

    else:
        db.execute("INSERT INTO users (username, hash) VALUES(?,?)", request.form.get("username"),
                   generate_password_hash(request.form.get("password")))

    return render_template("login.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    user_symbols = db.execute(
        "SELECT symbol FROM exchanges WHERE id=?", session["user_id"])
    if request.method == "GET":
        return render_template("sell.html", symbols=user_symbols)

    quote = lookup(request.form.get("symbol"))
    shares = request.form.get("shares")

    try:
        shares = int(shares)
    except:
        return apology("Las acciones deben ser un numero entero", 403)

    if shares <= 0:
        return apology("Las acciones deben ser mayores a cero", 403)

    user_shares = db.execute("SELECT shares FROM exchanges WHERE id=? AND symbol=?",
                             session["user_id"],
                             quote["symbol"])

    if not user_shares or int(user_shares[0]["shares"]) < shares:
        return apology("No tienes acciones suficientes")

    db.execute("INSERT INTO history (id, symbol, shares, price) VALUES(?,?,?,?)",
               session["user_id"],
               quote["symbol"],
               -shares,
               usd(quote["price"])
               )

    db.execute("UPDATE users SET cash=cash+ :increase WHERE id=:id",
               increase=usd(quote["price"] * float(shares)),
               id=session["user_id"])


    total_shares = user_shares[0]["shares"] - shares

    if total_shares == 0:
        db.execute("DELETE FROM exchanges WHERE id=? AND symbol=?",
                   session["user_id"], quote["symbol"])

    else:
        db.execute("UPDATE exchanges SET shares = :shares WHERE id= :id AND symbol= :symbol",
                   shares=total_shares, id=session["user_id"], symbol=quote["symbol"])

        total_ = (total_shares * quote["price"])
        db.execute("UPDATE exchanges SET total = :total WHERE id= :id AND symbol= :symbol",
                   total=usd(total_), id=session["user_id"], symbol=quote["symbol"])

    return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)