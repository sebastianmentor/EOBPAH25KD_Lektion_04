import json
from datetime import datetime

# Global dictionary to store accounts: {account_number: {"saldo": float, "transactions": list}}
accounts = {}

def create_account(account_number):
    """Create a new account with the given account number."""
    if account_number in accounts:
        raise ValueError("Account already exists.")
    accounts[account_number] = {"saldo": 0.0, "transactions": []}

def deposit(account_number, amount):
    """Deposit money into the specified account."""
    if account_number not in accounts:
        raise ValueError("Account does not exist.")
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")
    accounts[account_number]["saldo"] += amount
    accounts[account_number]["transactions"].append({
        "timestamp": datetime.now(),
        "type": "deposit",
        "amount": amount
    })

def withdraw(account_number, amount):
    """Withdraw money from the specified account if sufficient saldo."""
    if account_number not in accounts:
        raise ValueError("Account does not exist.")
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    if accounts[account_number]["saldo"] < amount:
        raise ValueError("Insufficient saldo.")
    accounts[account_number]["saldo"] -= amount
    accounts[account_number]["transactions"].append({
        "timestamp": datetime.now(),
        "type": "withdraw",
        "amount": amount
    })

def get_transactions(account_number):
    """Retrieve transaction data for the specified account."""
    if account_number not in accounts:
        raise ValueError("Account does not exist.")
    return accounts[account_number]["transactions"]

def get_saldo(account_number):
    """Retrieve the current saldo of the specified account."""
    if account_number not in accounts:
        raise ValueError("Account does not exist.")
    return accounts[account_number]["saldo"]

def save_accounts_to_file(filepath):
    """Save the accounts data to a file."""
    with open(filepath, 'w') as file:
        # Convert datetime objects to strings for JSON serialization
        json.dump(accounts, file, default=str)

def load_accounts_from_file(filepath):
    """Load the accounts data from a file."""
    global accounts
    with open(filepath, 'r') as file:
        data = json.load(file)
        # Convert timestamp strings back to datetime objects
        for account in data.values():
            for transaction in account["transactions"]:
                transaction["timestamp"] = datetime.fromisoformat(transaction["timestamp"])
        accounts = data