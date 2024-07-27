#!/usr/bin/python3
"""Add number route"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cIsFun(text):
    """Route for c

    Args:
        text (string): text will apear after c

    Returns:
        string: the text will be c <text>
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """two routes, it will return 'python <text>'"""
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display 'n is a number' only if n is an integer"""
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
