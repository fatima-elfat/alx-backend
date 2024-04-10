#!/usr/bin/env python3
"""
task 4 : Force locale with URL parameter.
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
def task05() -> str:
    """
    “Welcome to Holberton” as page title.
    """
    return render_template("4-index.html")


# works for version lower than 3.
@babel.localeselector
def get_locale() -> str:
    """
    detect if the incoming request contains
    locale argument and ifs value is a supported locale,
    return it. If not or if the parameter is not present,
    resort to the previous default behavior.
    """
    req = request.args.get('locale')
    if req in app.config['LANGUAGES']:
        return req
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
    )


if __name__ == "__main__":
    app.run()
