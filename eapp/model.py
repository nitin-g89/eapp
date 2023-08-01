from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Admin(db.Model):
    adminid = db.Column(db.Integer(),primary_key=True)
    email = db.Column(db.String(50),nullable=False,unique=True)
    password = db.Column(db.String(20),nullable=False)

class User(db.Model):
    userid = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(), unique=False, nullable=False)
    email = db.Column(db.String(50), nullable=False,unique=True)
    password = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(10), nullable=False)

class Category(db.Model):
    categoryid = db.Column(db.Integer(),primary_key=True)
    category_name = db.Column(db.String(100),nullable=False)
    products = db.relationship('Product',backref = "category")

class Product(db.Model):
    productid = db.Column(db.Integer(),primary_key = True)
    product_name = db.Column(db.String(100),nullable=False)
    image = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer(),nullable=False)
    unit  = db.Column(db.String(10),nullable=False)
    cat_id = db.Column(db.Integer(),db.ForeignKey("category.categoryid"))

class Order(db.Model):
    orderid = db.Column(db.Integer(), primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Integer(), nullable=False)
    buyerid = db.Column(db.Integer(),db.ForeignKey("user.userid"),nullable=False)

class OrderedProduct(db.Model):
    serialno = db.Column(db.Integer(), primary_key=True)
    orderid = db.Column(db.Integer(),db.ForeignKey('order.orderid'), nullable=False)
    productid = db.Column(db.Integer(),db.ForeignKey('product.productid'), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)

class Cart(db.Model):
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'), nullable=False, primary_key=True)
    productid = db.Column(db.Integer, db.ForeignKey('product.productid'), nullable=False, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)    


"""buy_weight = db.Column(db.Integer(),nullable=False)
    buy_unit = db.Column(db.String(),nullable=False)"""
