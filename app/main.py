from flask import Flask, redirect, url_for, render_template

from .api import get_teamnames, users, rosters

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", teamnames=get_teamnames(users))


@app.route("/pointswins")
def pointswins():
    return render_template("pointswins.html")


@app.route("/pointspercentage")
def pointspercentage():
    return render_template("pointspercentage.html")


@app.route("/winspercentage")
def winspercentage():
    return render_template("winspercentage.html")


# redirects to home if url is not found
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('home'))
