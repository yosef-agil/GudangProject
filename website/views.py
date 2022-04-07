from flask import Blueprint, render_template
from connectdb import Database

# define the file is blueprint
views = Blueprint('views', __name__)

@views.route('/', methods=["GET"])
def home():
    conn = Database('ksb-2022')
    func = conn.selectdata()
    return render_template("home.html", value=func)