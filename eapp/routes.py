from eapp import app
from eapp.model import *
from eapp.forms import *
from flask import render_template,request

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if isUserAdmin(email,password):
            return redirect(url_for('admin'))
        elif is_valid(email,password):
            session['email'] = email
            return redirect(url_for('home'))
        else:
            error = 'Invalid Email / Password'
            return render_template('login.html', error = error)
    
    if isUserLoggedIn():
        return redirect(url_for('home'))
    return render_template('login.html',error='')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        if request.form['password']==request.form['confirm-password']:
            msg = checkAndRegister(request)
            return render_template("login.html",error=msg)
        return render_template('register.html',error="Passwords do not match. Please re-enter.")    
    if isUserLoggedIn():
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route("/")
def home():
    if isUserLoggedIn():
        CategoryData = getCategoryDetails()
        userId = getuserId()
        return render_template("home.html",userid=userId,CategoryData = CategoryData)
    return redirect(url_for('login'))


