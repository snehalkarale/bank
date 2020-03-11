from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/dbemp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

bank_cust = db.Table(
    "BankCustomers",
    db.Column('cid', db.Integer(), db.ForeignKey('customer.id')),
    db.Column('bid', db.Integer(), db.ForeignKey('bank.id'))
)

class Bank(db.Model):
    id = db.Column('id', db.Integer(),primary_key=True)
    name = db.Column('name', db.String(100))
    active=db.Column('active',db.String(10),default='Y')
    aid=db.Column('adr_id',db.Integer(),db.ForeignKey("address.id"),unique=True)
    customers=db.relationship('Customer',secondary=bank_cust,backref='banks',lazy=True)

class Account(db.Model):
    id=db.Column('id',db.Integer(),primary_key=True)
    type=db.Column('type',db.String(100))
    balance=db.Column('balance',db.Integer())
    active=db.Column('active',db.String(100),default='Y')
    custid=db.Column('cust_id',db.Integer(),db.ForeignKey('customer.id'),unique=False)


class Customer(db.Model):
    id=db.Column('id',db.Integer(),primary_key=True)
    name=db.Column('name',db.String(100))
    gender=db.Column('gender',db.String(100))
    email=db.Column('email',db.String(100))
    age=db.Column('age',db.Integer())
    active=db.Column('active',db.String(100),default='Y')
    aid = db.Column('adr_id', db.Integer(), db.ForeignKey("address.id"), unique=True)
    accounts=db.relationship('Account',uselist=True,backref='customer',lazy=True)

class Address(db.Model):
    id=db.Column('id',db.Integer(),primary_key=True)
    city=db.Column('city',db.String(100))
    state=db.Column('state',db.String(100))
    pincode=db.Column('pincode',db.Integer())
    active=db.Column('active',db.String(100),default='Y')
    cust=db.relationship('Customer',backref='address',lazy=True)


if __name__ == '__main__':
    pass
    #db.create_all()