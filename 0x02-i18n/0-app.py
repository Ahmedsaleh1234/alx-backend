#!/usr/bin/env python3
"""0. Basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """route and an index.html template"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
