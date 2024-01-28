#!/usr/bin/python3

"""
Starts a Flask web application
"""

from flask import Flask

my_flask_app = Flask(__name__)


@my_flask_app.route('/', strict_slashes=False)
def greeting_hbnb():
    """Returns Hello HBNB!"""
    return 'Hello HBNB!'


@my_flask_app.route('/hbnb', strict_slashes=False)
def disp_hbnb():
    """Returns HBNB"""
    return 'HBNB'


@my_flask_app.route('/c/<text>', strict_slashes=False)
def c_is_fun(txt):
    """Display “C ” followed by the value of text variable"""
    return 'C ' + txt.replace('_', ' ')


@my_flask_app.route('/python', strict_slashes=False)
@my_flask_app.route('/python/<text>', strict_slashes=False)
def python_is_cool(txt='is cool'):
    """Display “Python ”, followed by the value of text variable"""
    return 'Python ' + txt.replace('_', ' ')


if __name__ == '__main__':
    my_flask_app.run(host='0.0.0.0', port='5000')
