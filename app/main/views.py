from flask import render_template, Blueprint
from flask_login import login_required


main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/secret')
@login_required
def secret():
    return "<h1>SECRET PAGE ACCESSED!</h1>"
