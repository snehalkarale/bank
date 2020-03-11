from Flask.Bank_statement.models import *
from Flask.Bank_statement.dao import BankDao

MIN_BALANCE=10000

class BankCrudOp(BankDao):

    def get_all_active_customers(self):
        return Customer.query.filter(Customer.active=='Y').all()

    def get_active_customer(self,cid):
        return Customer.query.filter(Customer.active=='Y', Customer.id==cid).first()

    def get_all_active_accounts(self,cid):
        customer=self.get_active_customer(cid)
        if customer:
            accountList=[]
            for acc in customer.accounts:
                if acc.accounts=='Y':
                    accountList.append(acc)
            return accountList
        else:
            print("customer not available...")

    def get_active_account(self,cid,aid):
        customer=self.get_active_customer(cid)
        if customer:
            account=Account.query.filter(Account.active=='Y',Account.id=='aid').first()
            if account:
                if account.custid==cid:
                    return account
                else:
                    print("no account with customer...")
            else:
                print("No account with given Id")
        else:
            print("customer not present...")

    def bank_capital(self):
        accounts=Account.query.filter(Account.custid!=None).all()
        sum=0
        for acc in accounts:
            sum+=acc.balance
        return sum

    def withdraw_amount(self,amount,dbacc):
        try:
            existingBal=dbacc.balance
            dbacc.balance=existingBal-amount
            db.session.commit()
            return True
        except:
            return False

    def deposit_amout(self,amount,dbacc):
        try:
            existingBal=dbacc.balance
            dbacc.balance=existingBal+amount
            db.session.commit()
            return True
        except:
            return False

    def duplicateAddress(self,adrid):
        if Customer.query.filter(Customer.id==adrid).first():
            return True
        else:
            return False

    def duplicateEmail(self,email):
        if Customer.query.filter(Customer.email==email).first():
            return True
        else:
            return False

    def add_customer(self,custModel):
        db.session.add(custModel)
        db.session.commit()
        return "customer added successfully..."

    def update_cutomer(self):
        pass

    def get_active_addresses(self):
        return Address.query.filter(Address.active=='Y').all()