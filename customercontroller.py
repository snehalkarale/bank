from Flask.Bank_statement.models import app, Customer
from flask import Flask, render_template, request
from Flask.Bank_statement.serviceimpl import BankServiceImpl

service = BankServiceImpl
genderTypes = {"M": "Male", "F": "Female"}


class custval:
    def __init__(self, cid, cname, cage, cgender, cemail, adr):
        self.cid = cid
        self.cname = cname
        self.cage = cage
        self.cgender = cgender
        self.email = cemail
        self.adr = int(adr)


def dummycust():
    return custval(cid=0, cname='', cage=0, cgender='', cemail='', adr='0')


@app.route("/customer/welcome/",methods=["GET"])
def welcome_customer():
    return render_template('customer.html', custs=Customer.query.filter(Customer.active == 'Y').all(),
                           genders=genderTypes, cust=dummycust(),
                           addresses=service.get_all_active_address())


@app.route("/customer/persist/",methods=["POST"])
def save_customer_info():
    print(request.form)
    msg = service.add_customer(request.form)
    if "successfully" not in msg:
        cust = custval(**request.form)
    else:
        cust = dummycust()
    return render_template('customer.html', custs=Customer.query.filter(Customer.acive == 'Y').all(),
                           gender=genderTypes, msg=msg,
                           cust=cust,
                           addresses=service.get_all_active_address())


if __name__ == '__main__':
    app.run(debug=True)
