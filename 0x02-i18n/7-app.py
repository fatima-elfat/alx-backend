#!/usr/bin/env python3
"""
task 7 : Infer appropriate time zone.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, exceptions
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
def task07() -> str:
    """
    “Welcome to Holberton” as page title.
    """
    return render_template("7-index.html")


# works for version lower than 3.
@babel.localeselector
def get_locale() -> str:
    """
    Change your get_locale function to use a user’s
    preferred local if it is supported.
    The order of priority should be
        Locale from URL parameters
        Locale from user settings
        Locale from request header
        Default locale
    """
    req = request.args.get('locale')
    if req in app.config['LANGUAGES']:
        return req
    if g.user and g.user.get('locale'):
        if g.user.get('locale') in app.config['LANGUAGES']:
            return g.user.get('locale')
    req = request.headers.get('locale', '')
    if req in app.config["LANGUAGES"]:
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
def before_request()-> None:
    """
    use get_user to find a user if any.
    """
    g.user = get_user()


@babel.timezoneselector
def get_timezone() -> str:
    """
    The logic should be the same as get_locale:
        Find timezone parameter in URL parameters
        Find time zone from user settings
        Default to UTC
    """
    val = request.args.get('timezone', '').strip()
    if not val and g.user:
        if g.user.get("timezone"):
            val = g.user.get("timezone")
    try:
        return timezone(val).zone
    except exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == "__main__":
    app.run()
