from flask import Blueprint
from flask import render_template
from flask import abort
from jinja2 import TemplateNotFound

mod_base = Blueprint('mod_base', __name__,
                     template_folder='templates')


@mod_base.route('/', defaults={'page': 'index'})
@mod_base.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
