# This file simulates a bank worker module.
# It provides a reusable function to process transactions.
# This file should NOT be executed directly — it is meant to be imported by other scripts.

# Function to simulate processing a bank transaction
def process_transaction(customer_name, amount):
    print(f"[bank_worker] Processed transaction for {customer_name}: ${amount:.2f}")

# This line runs regardless of how the file is used
print("[bank_worker] Worker module loaded.")

# Main guard: only runs when this file is executed directly
if __name__ == "__main__":
    print("[bank_worker] WARNING: This module is not meant to be run directly.")
    print("[bank_worker] Please use bank_manager_example.py to initiate transactions.")
