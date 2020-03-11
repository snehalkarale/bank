
from abc import ABC,abstractmethod

class BankDao(ABC):
    @abstractmethod
    def get_all_active_customers(self):
        pass

    @abstractmethod
    def get_active_customer(self,cid):
        pass

    @abstractmethod
    def bank_capital(self):
        pass

    @abstractmethod
    def withdraw_amount(self,amount,account):
        pass

    @abstractmethod
    def deposit_amout(self,amount,account):
        pass

    @abstractmethod
    def add_customer(self,custModel):
        pass

    @abstractmethod
    def update_cutomer(self):
        pass

    @abstractmethod
    def get_active_addresses(self):
        pass