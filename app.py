from flask import Flask, redirect, url_for

from api import get_owners, data

app = Flask(__name__)

@app.route("/")
def home():
    return f"<h1>HELLO</h1> {get_owners(data)}"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()