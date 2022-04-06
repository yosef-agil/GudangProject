from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>This is logut</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        fullName = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email is invalid.', category='error')
        elif len(fullName) < 2:
            flash('This is not the correct name.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 character', category='error')
        else:
            # add user to database
            flash('Account Successfully Created', category='success')

    return render_template("sign_up.html")

@auth.route('/addProduct', methods=['GET', 'POST'])
def addProduct():
    return render_template("addProduct.html")