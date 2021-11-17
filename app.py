from flask import Flask, redirect, url_for

from api import get_teamnames, users, rosters

app = Flask(__name__)


@app.route("/")
def home():
    return f"<h1>Teams</h1> {get_teamnames(users)}"


# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
