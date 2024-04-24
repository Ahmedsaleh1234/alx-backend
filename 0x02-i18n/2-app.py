#!/usr/bin/env python3
"""2. Get locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    """to config babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE= "UTC"

app = Flask(__name__)

app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app, locale_selector=get_locale)




def get_locale() -> str:
    """ to determine the best match with our supported languages."""
    return request.accept_language.best_matche(app.config['LANGUAGE'])

@app.route('/')
def index() -> str:
    """return index"""
    return render_template('2-index.html')
    

if __name__ == '__main__':
    app.run()
