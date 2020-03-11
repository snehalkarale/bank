
from abc import ABC,abstractmethod

class BankServices(ABC):

    @abstractmethod
    def withdraw_amount(self,bank,amount,accno):
        pass

    @abstractmethod
    def deposit_amount(self,bank,amount,accno):
        pass

    @abstractmethod
    def add_customer(self,cust):
        pass

    @abstractmethod
    def update_cutomer(self,cust):
        pass

    @abstractmethod
    def duplicateAddress(self,adrid):
        pass

    @abstractmethod
    def find_duplicate_email(self,email):
        pass

    @abstractmethod
    def get_all_active_address(self):
        pass