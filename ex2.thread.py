#simulate a shared bank account . 2 threads= account holders
# both withdraw funds simul. account balance is synchronized properly to prevent race condition

# withdraw method with lock to sync access and prevent race condition ()

import threading 
import time

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            currentbalance=self.balance
            if amount <=currentbalance:
                new_balance= currentbalance+amount
                self.balance= new_balance
                print(f"Withdrawal successful with new balance {new_balance}")
            else:
                print("Unsuccesful")

def account_holder(account, amount):
    for i in range(3):
        account.withdraw(amount)

if __name__ == "__main__":
    shared_account= BankAccount(100000)
    thread_holder1=threading.Thread(target=account_holder, args=(shared_account, 300))
    thread_holder2=threading.Thread(target=account_holder, args=(shared_account, 200))

    thread_holder1.start()
    thread_holder2.start()

    thread_holder1.join()
    thread_holder2.join()

