#!/usr/bin/python3
<<<<<<< HEAD
"""
    Sript that starts a Flask web application
 """
=======
<<<<<<< HEAD
"""
start Flask application
"""

>>>>>>> 2f0813143d9d93724458ff791ae5501a83b7fc94
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello_hbn():
    """
        function to return Hello HBNB!
    """
    return "Hello HBNB!"
=======
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'
>>>>>>> 2f0813143d9d93724458ff791ae5501a83b7fc94


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """
        function to return HBNB
    """
    return "HBNB"
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
=======
    """returns HBNB"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 43a24faa69bbd151b8fec987ee56df7de02c39b7
>>>>>>> 2f0813143d9d93724458ff791ae5501a83b7fc94
