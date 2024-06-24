#!/usr/bin/python3
<<<<<<< HEAD
"""
    Sript that starts a Flask web application
"""
from flask import Flask, render_template
=======
<<<<<<< HEAD
"""
start Flask application
"""

from flask import Flask, render_template
from models import *
>>>>>>> 2f0813143d9d93724458ff791ae5501a83b7fc94
from models import storage
app = Flask(__name__)


<<<<<<< HEAD
@app.teardown_appcontext
def handle_teardown(self):
    """
        method to handle teardown
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """
        method to render states
    """
    states = storage.all('State').values()
    return render_template("7-states_list.html", states=states)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
=======
@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.

    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
>>>>>>> 43a24faa69bbd151b8fec987ee56df7de02c39b7
>>>>>>> 2f0813143d9d93724458ff791ae5501a83b7fc94
