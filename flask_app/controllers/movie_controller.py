from flask import render_template
from flask_app import app

# Testing route only
@app.route("/")
def test_route():
    return render_template("test_html.html", title = "Home page", user = {"name": "Peter"})