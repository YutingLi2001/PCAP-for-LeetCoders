# This script represents the bank manager.
# It imports the bank worker module and prepares a transaction.
# Your task is to add a main guard so that the transaction only runs when this file is executed directly.

import bank_worker

customer_name = "Alice"
transaction_amount = 1500.00

def run_daily_transaction():
    print("[bank_manager] Starting daily transaction task...")
    bank_worker.process_transaction(customer_name, transaction_amount)
    print("[bank_manager] Transaction completed.")

# TODO: 
# Use a main guard below to ensure that the run_daily_transaction() function
# is only executed when this file is run directly (not when imported)

# 🤔 Reflection:
# What would happen if someone else imports this file into another script?
# What part of the code would still run, and what part would be skipped?

# ✅ When you're ready, you can test your solution automatically using the command below:
# > py tests/04_functions_exceptions_test/main_guard_test/01_bank_transaction_guard_test.py
# This script will check whether your output matches the expected behavior.