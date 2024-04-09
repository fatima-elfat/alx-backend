#!/usr/bin/env python3
"""
task 0 : Basic Flask app.
"""
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET"], strict_slashes=False)
def task00() -> str:
    """
    “Welcome to Holberton” as page title.
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
