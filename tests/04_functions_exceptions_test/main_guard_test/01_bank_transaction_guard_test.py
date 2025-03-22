# 📁 File: test_bank_manager.py
# 🔍 Automated test script for bank_manager.py

import subprocess
import os

# 🔧 Locate the target exercise file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
exercise_path = os.path.abspath(os.path.join(
    BASE_DIR,
    "../../../04_functions_exceptions/main_guard/exercises/01_bank_transaction_guard/bank_manager.py"
))

# ✅ Expected output lines when the file is run directly
EXPECTED_OUTPUT = [
    "[bank_worker] Worker module loaded.",
    "[bank_manager] Starting daily transaction task...",
    "[bank_worker] Processed transaction for Alice: $1500.00",
    "[bank_manager] Transaction completed."
]

# ✅ Expected output when bank_manager is imported
EXPECTED_IMPORT_OUTPUT = [
    "[bank_worker] Worker module loaded."
]

def run_script():
    try:
        result = subprocess.run(
            ["python", exercise_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip().splitlines()
    except Exception as e:
        return [f"Error during execution: {e}"]

def run_import():
    try:
        result = subprocess.run(
            ["python", "-c", "import bank_manager"],
            capture_output=True,
            text=True,
            timeout=5,
            cwd=os.path.dirname(exercise_path)  # ensure import from correct location
        )
        return result.stdout.strip().splitlines()
    except Exception as e:
        return [f"Error during import test: {e}"]

def check_output(actual_lines):
    print("\n=== Test 1: Direct Execution Output ===")
    score = 0
    total = len(EXPECTED_OUTPUT)

    for i, expected in enumerate(EXPECTED_OUTPUT):
        if i < len(actual_lines) and expected in actual_lines[i]:
            print(f"Line {i+1}: ✅ {expected}")
            score += 1
        else:
            actual = actual_lines[i] if i < len(actual_lines) else "(no output)"
            print(f"Line {i+1}: ❌")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")

    print(f"\nScore: {score}/{total}")
    return score == total

def check_import_behavior(import_lines):
    print("\n=== Test 2: Import Behavior Output ===")
    if import_lines == EXPECTED_IMPORT_OUTPUT:
        print("✅ Import behavior is correct (main logic did not execute).")
        return True
    else:
        print("❌ Import triggered execution that should be guarded by main.")
        print("Output during import:")
        for line in import_lines:
            print("  ", line)
        return False

if __name__ == "__main__":
    run_lines = run_script()
    direct_pass = check_output(run_lines)

    import_lines = run_import()
    import_pass = check_import_behavior(import_lines)

    print("\n=== Final Result ===")
    if direct_pass and import_pass:
        print("🎉 All tests passed!")
    else:
        print("⚠️ One or more tests failed.")