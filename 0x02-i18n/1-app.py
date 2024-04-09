#!/usr/bin/env python3
"""1. Basic Babel setup"""

from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """ set Babel’s default l"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """configure available languages in our app"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
