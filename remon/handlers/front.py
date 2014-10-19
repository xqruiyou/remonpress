# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort

home_bp = Blueprint("home", __name__)

@home_bp.route('/')
def home():
    try:
        return render_template('index.html', name = name)
    except TemplateNotFound:
        abort(404)