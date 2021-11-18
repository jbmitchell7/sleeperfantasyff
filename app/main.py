from flask import Flask, redirect, url_for, render_template

from .api import teamnames
from .chart import pw_graph, pp_graph, wp_graph

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html", teamnames=teamnames)


@app.route("/charts")
def charts():
    return render_template("charts.html", pw_graph=pw_graph, pp_graph=pp_graph, wp_graph=wp_graph)


# redirects to home if url is not found
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('home'))
