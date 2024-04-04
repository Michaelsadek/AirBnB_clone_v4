#!/usr/bin/python3
"""Simple Flask web application"""
from flask import Flask
app = Flask(__name__)

#Define the route for  the root URL'/'

@app.route('/', strict_slashes=False)
def hello_route():
    """Return simple string"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    #Start the Flask development server
    #Listen on all available network interfaces (0.0.0.0) and port 500
    app.run(host='0.0.0.0', port=5000)
