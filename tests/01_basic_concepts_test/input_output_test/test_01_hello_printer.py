import subprocess

EXPECTED_OUTPUT = [
    "Hello, I am programming in Python!",
    "Welcome to PCAP Prep!",
    "This is Exercise 01.",
    "Name: Alice Age: 23",
    "Loading...Done"
]

def run_user_script():
    try:
        result = subprocess.run(
            ["python", "01_hello_printer.py"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip().splitlines()
    except Exception as e:
        return [f"Error: {e}"]

def check_output(actual_lines):
    score = 0
    total = len(EXPECTED_OUTPUT)

    print("=== Test Results ===")
    for i, expected in enumerate(EXPECTED_OUTPUT):
        if i < len(actual_lines) and expected in actual_lines[i]:
            print(f"Step {i+1}: ✅ Passed")
            score += 1
        else:
            print(f"Step {i+1}: ❌ Failed")
            print(f"  Expected: {expected}")
            actual = actual_lines[i] if i < len(actual_lines) else "(No Output)"
            print(f"  Actual:   {actual}")
    print(f"\nScore: {score}/{total}")

if __name__ == "__main__":
    output_lines = run_user_script()
    check_output(output_lines)
