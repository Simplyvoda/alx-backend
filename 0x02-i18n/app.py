#!/usr/bin/env python3
'''
Basic Babel setup
'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import Union, Dict
import pytz
from datetime import datetime


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Class for Babel Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
app.url_map.strict_slashes = False

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Union[Dict, None]:
    """function to get the user from mock user objecrs
    
    Keyword arguments:
    argument -- none
    Return: user object or None
    """
    user_id = request.args.get("login_as", "")
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """decorator function that runs before the request
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Function that retrieves the locale language from parameter, setting
    or request headers accordingly
    """
    locale_from_url = request.args.get('locale')
    if locale_from_url and locale_from_url in app.config['LANGUAGES']:
        return locale_from_url

    if g.user and 'locale' in g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']


    header_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if header_locale:
        return header_locale

    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """
    Function that retrieves the timezone from parameter, setting
    or request headers accordingly
    """
    timezone_from_url = request.args.get('timezone', '').strip()
    if timezone_from_url:
        try:
            pytz.timezone(timezone_from_url)
            return timezone_from_url
        except pytz.exceptions.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']
    
    if g.user and 'timezone' in g.user:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']

    return app.config['BABEL_DEFAULT_TIMEZONE']
    

@app.route('/')
def index() -> str:
    """
    The index page
    using _ function to translate text
    """
    current_time = format_datetime()
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
