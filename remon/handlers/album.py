# -*- coding: utf-8 -*-
# Collection of content

from flask import Blueprint, render_template, abort

album_bp = Blueprint("album", __name__)

@album_bp.route('/album/<album_name>')
def album(album_name):
    try:
        render_template("", name = name)
    except TemplateNotFound:
        abort(404)