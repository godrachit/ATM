def add_transaction(account, message):
    account.transactions.append(message)


def show_statement(account):
    if not account.transactions:
        print("No transactions yet.")
    else:
        print("\n--- Statement ---")
        for t in account.transactions:
            print(t)