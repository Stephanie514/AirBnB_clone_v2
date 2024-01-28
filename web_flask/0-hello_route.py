#!/usr/bin/python3
""" Starts a Flash Web Application """

from flask import Flask as MyFlask

my_app = MyFlask(__name__)


@my_app.route('/', strict_slashes=False)
def custom_greeting():
    """Prints a Message when / is called"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    """Main Function"""
    my_app.run(host='0.0.0.0', port=5000)
