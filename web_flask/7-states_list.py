#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage as st

app = Flask(__name__)


@app.route('/states_listing', strict_slashes=False)
def states_listing():
    """Display a HTML page with the states listed in alphabetical order"""
    states_data = sorted(list(st.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_listing.html', states_data=states_data)


@app.teardown_appcontext
def teardown_db_context(exception):
    """Closes the storage on teardown"""
    st.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
