from flask import Flask,render_template,request
from Flask.Bank_statement.models import app
from Flask.Bank_statement.serviceimpl import BankServiceImpl

service=BankServiceImpl

@app.route("/cust/<int:cid>/account/<int:aid>",methods=["GET"])
def get_account_balance(cid,aid):
    dbaccount=service.get_active_account(cid,aid)
    if dbaccount:
        print(dbaccount)

@app.route("/cust/<int:cid>",methods=["GET"])
def get_customer_balance(cid):
    dbaccount=service.get_all_active_account(cid)
    if dbaccount:
        print(dbaccount)

if __name__ == '__main__':
    app.run(debug=True)
    print(get_account_balance(111,2))