from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/search/player/<name>")
def search_player(name):
    # Prototype placeholder — DB queries will go here
    results = [{"player": name, "year": 1958, "set": "Alifabolaget"}]
    return render_template("search_results.html", cards=results)

