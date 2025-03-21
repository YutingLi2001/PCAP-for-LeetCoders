import subprocess
import os

# 🔧 Build the absolute path to the exercise script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
exercise_path = os.path.abspath(os.path.join(
    BASE_DIR,
    "../../../01_basic_concepts/input_output/exercises/01_hello_printer.py"
))

def run_user_script():
    try:
        result = subprocess.run(
            ["python", exercise_path],
            capture_output=True,
            text=True,
            timeout=5
        )

        print("=== Raw Output ===")
        print("STDOUT:")
        print(result.stdout)
        print("STDERR:")
        print(result.stderr)

        return result.stdout.strip().splitlines()
    except Exception as e:
        return [f"Error: {e}"]

def check_output(lines):
    score = 0
    total = 4

    print("\n=== Test Results ===")
    print(f"Detected {len(lines)} total output lines.")

    # Step 1: Any output is acceptable
    if len(lines) >= 1:
        print("Step 1: ✅ Passed")
        score += 1
    else:
        print("Step 1: ❌ Failed - No output detected")

    # Step 2: Must have exactly 2 non-empty lines after Step 1
    if len(lines) >= 3:
        step2 = lines[1:3]
        print(f"Step 2 candidate lines:\n1: {step2[0]!r}\n2: {step2[1]!r}")
        if len(step2) == 2 and all(line.strip() for line in step2):
            print("Step 2: ✅ Passed")
            score += 1
        else:
            print("Step 2: ❌ Failed - Step 2 must have exactly 2 non-empty lines")
    else:
        print("Step 2: ❌ Failed - Not enough output lines for Step 2")

    # Step 3: Output must contain both "New York" and "2025"
    found = False
    for line in lines:
        if "New York" in line and "2025" in line:
            found = True
            break
    if found:
        print("Step 3: ✅ Passed")
        score += 1
    else:
        print("Step 3: ❌ Failed - Must contain both 'New York' and '2025'")

    # Step 4: Must contain exact line: 2-3-4-5-6-7
    if any(line.strip() == "2-3-4-5-6-7" for line in lines):
        print("Step 4: ✅ Passed")
        score += 1
    else:
        print("Step 4: ❌ Failed - 2-3-4-5-6-7 output not found")

    print(f"\nScore: {score}/{total}")

if __name__ == "__main__":
    output_lines = run_user_script()
    check_output(output_lines)
