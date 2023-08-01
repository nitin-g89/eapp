from flask import session,url_for,redirect
from eapp.model import *

def is_valid(email,password):
    user = User.query.filter_by(email = email).first()
    if user and user.password==password:
        return True
    return False

def isUserAdmin(email,pswrd):
    user = Admin.query.filter_by(email=email).first()
    if user and user.password==pswrd:
        return True
    return False

def checkAndRegister(request):
    email = request.form['email']
    user = User.query.filter_by(email = email).first()
    if not user:
        name = request.form['name']
        password = request.form['password']
        phone = request.form['phone']
        address = request.form['address']
        newUser = User(name=name,email=email,password=password,
                       address=address,phone=phone)

        db.session.add(newUser)
        db.session.flush()
        db.session.commit()
        
        return "Registered Successfully"
    return "Email is already Registered"

def isUserLoggedIn():
    if 'email' not in session:
        return False
    else:
        return True
    
def getCategoryDetails():
    catData = Category.query.all()
    return catData

def getuserId():
    user = User.query.filter_by(email = session['email']).first()
    return user.userid