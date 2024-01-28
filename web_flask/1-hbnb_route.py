#!/usr/bin/python3
"""Starts a Flask Web Application HBNB"""

from flask import Flask

my_flask_app = Flask(__name__)


@my_flask_app.route('/', strict_slashes=False)
def greeting_hbnb():
    """Prints a Message when / is called"""
    return 'Hello HBNB!'


@my_flask_app.route('/hbnb', strict_slashes=False)
def disp_hbnb():
    """Prints a Message when /hbnb is called"""
    return 'HBNB'


if __name__ == "__main__":
    my_flask_app.run(host='0.0.0.0', port=5000)
