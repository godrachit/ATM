from atm.statement import add_transaction

def deposit(account):
    amount = float(input("Enter amount to deposit: "))
    account.update_balance(amount)
    add_transaction(account, f"Deposited: ₹{amount}")
    print("Deposit successful!")

def withdraw(account):
    amount = float(input("Enter amount to withdraw: "))
    if amount > account.get_balance():
        print("Insufficient balance!")
    else:
        account.update_balance(-amount)
        add_transaction(account, f"Withdrawn: ₹{amount}")
        print("Withdrawal successful!")

def check_balance(account):
    print(f"Current Balance: ₹{account.get_balance()}")