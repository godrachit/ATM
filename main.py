from atm.account import Account
from atm.operations import deposit, withdraw, check_balance
from atm.statement import show_statement

def main():
    account = Account()

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Statement")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            check_balance(account)

        elif choice == "2":
            deposit(account)

        elif choice == "3":
            withdraw(account)

        elif choice == "4":
            show_statement(account)

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()