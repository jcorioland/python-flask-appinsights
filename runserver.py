"""
This script runs the FlaskWebApp application using a development server.
"""

from os import environ
from FlaskWebApp import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5556'))
    except ValueError:
        PORT = 5556
    app.run(HOST, PORT)
