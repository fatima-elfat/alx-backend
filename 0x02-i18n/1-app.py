#!/usr/bin/env python3
"""
task 1 : Basic Babel setup.
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__, template_folder="templates")
babel = Babel(app)


class Config(object):
    """
    create a Config class that has a
    LANGUAGES class attribute equal to ["en", "fr"].
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=["GET"], strict_slashes=False)
def task01() -> str:
    """
    “Welcome to Holberton” as page title.
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
