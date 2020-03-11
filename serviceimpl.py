from Flask.Bank_statement.models import Customer
from Flask.Bank_statement.daoimpl import BankCrudOp
from Flask.Bank_statement.service import BankServices
bankPersistInstance=None

class BankServiceImpl(BankServices):
    def __init__(self):
        global bankPersistInstance
        bankPersistInstance=BankCrudOp()

    def get_active_account(self,cid,aid):
        dbaccount=bankPersistInstance.get_active_account(cid,aid)
        if dbaccount:
            return dbaccount

    def get_all_active_account(self,cid):
        dbaccount=bankPersistInstance.get_all_active_accounts(cid)
        if dbaccount:
            return dbaccount

    def withdraw_amount(self,amount,accno):
        if amount>0:
            dbacc = self.get_active_account(accno)
            if dbacc and dbacc.balance-10000>amount:
                if bankPersistInstance.withdraw_amount(dbacc,amount):
                    return "Successful Transaction"
                else:
                    return "Transaction Failed"
            else:
                print("No account present or insufficient fund")
        else:
            print("Invalid Amount")

    def deposit_amount(self,amount,accno):
        if amount>0:
            dbacc=self.get_active_account(accno)
            if dbacc:
                if bankPersistInstance.deposit_amount(dbacc,amount):
                    return "succesful transaction"
                else:
                    return "Transaction Faild"
            else:
                print("no account present or insufficient fund")
        else:
            print("Invalid amount")

    def duplicateAddress(self,adrid):
        return bankPersistInstance.duplicateAddress(adrid)

    def findDuplicateEmail(self,email):
        return bankPersistInstance.findDuplicateEmail(email)

    def add_customer(self,cust):
        if cust:
            if not self.findDuplicateEmail(cust['ceml']):
                if not self.duplicateAddress(cust['adr']):
                    cust= Customer(name=cust['cnm'],
                                   gender=cust['gender'],
                                   age=cust['age'],
                                   email=cust['ceml'],
                                   aid=cust['adr'])
                    return bankPersistInstance.add_customer(cust)
                else:
                    return "Duplicate address.. aleready given to person"
            else:
                return "Duplicate email address.."
        else:
            return "invalid customer.."

    def update_customer(self,cust):
        pass

    def get_all_active_address(self):
        return bankPersistInstance.get_active_addresses()