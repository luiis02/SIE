from flask import Flask, Blueprint, redirect, url_for, request, render_template, send_file, send_from_directory, session, jsonify
from bd import DatabaseController
registro = Blueprint('registro', __name__)

@registro.route('/registro')
def register():
    return render_template('registro.html')