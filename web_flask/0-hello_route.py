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


<<<<<<< HEAD
@app.route('/', strict_slashes=False)
def hello_hbn():
    """
        function to return Hello HBNB!
    """
    return "Hello HBNB!"
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
=======
@app.route('/airbnb-onepage/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 43a24faa69bbd151b8fec987ee56df7de02c39b7
>>>>>>> 2f0813143d9d93724458ff791ae5501a83b7fc94
