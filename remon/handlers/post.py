# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort
from datetime import date

post_bp = Blueprint("post", __name__)

@post_bp.route('/post/<post_id>/<title>')
def post(post_id, title):
    now = date.today()
    for i in now:
        post_id += i.str()
    try:
        render_template("", name = name)
    except TemplateNotFound:
        abort(404)
