# -*- coding: utf-8 -*-

from flask import Flask
from remon.handlers.front import home_bp

def startup():
    app = Flask(__name__, template_folder = 'templates')
    app.register_blueprint(home_bp)

def main():
    startup()
    app.run(debug = True)

if __name__ == '__main__':
    main()