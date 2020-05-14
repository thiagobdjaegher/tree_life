from flask import render_template
from . import bl_home


@bl_home.route('/')
def index():
    return render_template('index.html')
