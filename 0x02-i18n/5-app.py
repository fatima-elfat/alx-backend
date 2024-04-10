#!/usr/bin/env python3
"""
task 5 : Mock logging in.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union

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
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route("/", methods=["GET"], strict_slashes=False)
def task05() -> str:
    """
    “Welcome to Holberton” as page title.
    """
    return render_template("5-index.html")


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


def get_user() -> Union[dict, None]:
    """
    Define a get_user function that returns a user dictionary or None if the
    ID cannot be found or if login_as was not passed.
    """

    try:
        user = int(request.args.get("login_as"))
        if user in users:
            user = users.get(user)
    except Exception:
        user = None
    return user


@app.before_request
def before_request() -> None:
    """
    use get_user to find a user if any.
    """
    g.user = get_user()


if __name__ == "__main__":
    app.run()
