from flask import Blueprint, render_template

contacto = Blueprint('contacto', __name__)

@contacto.route('/contacto')
def contacto_page():
    return render_template('contacto.html')
