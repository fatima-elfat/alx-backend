#!/usr/bin/env python3
"""
task 3 : Parametrize templates.
"""
from flask import Flask, render_template, request
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
def task03() -> str:
    """
    “Welcome to Holberton” as page title.
    """
    return render_template("3-index.html")


# works for version lower than 3.
@babel.localeselector
def get_locale() -> str:
    """
    determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
    )


if __name__ == "__main__":
    app.run()
