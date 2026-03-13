from atm import create_account, deposit, withdraw, get_saldo, get_transactions, save_accounts_to_file, load_accounts_from_file

def main():
    while True:
        print("\n--- ATM Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Saldo")
        print("5. View Transactions")
        print("6. Save Accounts to File")
        print("7. Load Accounts from File")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        try:
            if choice == "1":
                account_number = input("Enter account number: ")
                create_account(account_number)
                print("Account created successfully.")
            elif choice == "2":
                account_number = input("Enter account number: ")
                amount = float(input("Enter amount to deposit: "))
                deposit(account_number, amount)
                print("Deposit successful.")
            elif choice == "3":
                account_number = input("Enter account number: ")
                amount = float(input("Enter amount to withdraw: "))
                withdraw(account_number, amount)
                print("Withdrawal successful.")
            elif choice == "4":
                account_number = input("Enter account number: ")
                saldo = get_saldo(account_number)
                print(f"Current saldo: {saldo}")
            elif choice == "5":
                account_number = input("Enter account number: ")
                transactions = get_transactions(account_number)
                print("Transactions:")
                for transaction in transactions:
                    print(transaction)
            elif choice == "6":
                filepath = input("Enter file path to save accounts: ")
                save_accounts_to_file(filepath)
                print("Accounts saved successfully.")
            elif choice == "7":
                filepath = input("Enter file path to load accounts: ")
                load_accounts_from_file(filepath)
                print("Accounts loaded successfully.")
            elif choice == "8":
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
