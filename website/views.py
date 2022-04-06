from flask import Blueprint, render_template

# define the file is blueprint
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")