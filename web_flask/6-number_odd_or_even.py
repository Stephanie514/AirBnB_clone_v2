#!/usr/bin/python3

"""
This Starts a Flask web application
"""

from flask import Flask, render_template

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
def c_is_fun(text):
    """Displays “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@my_flask_app.route('/python', strict_slashes=False)
@my_flask_app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """Displays “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@my_flask_app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """Displays “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@my_flask_app.route('/number_template/<int:n>', strict_slashes=False)
def number_and_template(n):
    """Displays a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@my_flask_app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_and_evenness(n):
    """Displays a HTML page only if n is an integer"""
    evenness = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, evenness=evenness)


if __name__ == '__main__':
    my_flask_app.run(host='0.0.0.0', port='5000')
