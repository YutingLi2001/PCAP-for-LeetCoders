# 📘 Understanding `__name__` and `if __name__ == "__main__"`

## 🧠 What is `__name__` in Python?

Every Python module (i.e. `.py` file) has a built-in variable called `__name__`. This variable holds a **string** that tells you how the module is being used:

- If the file is being **run directly**, then `__name__` is set to:
  ```python
  "__main__"
  ```
- If the file is being **imported** as a module, then `__name__` is set to the **module's name** (i.e. the filename without `.py`)

---

## 🧪 Example 1: Running a script directly

```python
# file: hello.py
print("The value of __name__ is:", __name__)
```

When you run this file:
```bash
$ python hello.py
```

Output:
```
The value of __name__ is: __main__
```

---

## 📥 Example 2: Importing a script as a module

```python
# file: hello.py
print("hello.py says: __name__ is", __name__)
```
```python
# file: runner.py
import hello
print("runner.py is executing")
```

Now run:
```bash
$ python runner.py
```

Output:
```
hello.py says: __name__ is hello
runner.py is executing
```

Notice: `hello.py` was **imported**, so `__name__ == "hello"`.

---

## 🔐 Why use `if __name__ == "__main__"`?

Sometimes, you want part of your script to **only run when the file is executed directly**, but **not when it's imported**.

### ✅ Solution:
```python
# file: hello.py
def greet():
    print("Hello from function!")

if __name__ == "__main__":
    greet()
```

Now:
- Running `python hello.py` will print the greeting ✅
- Importing `hello` in another file will not automatically print anything ❌ (unless `greet()` is called)

This pattern is called the **main guard**.

---

## 🔄 Summary
| Situation                    | `__name__` value |
|-----------------------------|------------------|
| Run directly (`python x.py`) | `"__main__"`      |
| Imported as module          | module name      |


## 🧰 Best Practices
- Always wrap test/demo code in `if __name__ == "__main__":` block.
- This makes your file reusable as a module **and** executable as a script.

---

## ✅ You Should Be Able To:
- Explain what `__name__` does
- Use the main guard to protect executable logic
- Predict output when a file is run vs imported

---

## 🔁 Multi-File Example: Direct vs Import

We provide a real working pair of files to help you fully grasp the difference between **direct execution** and **module import**:

📁 Path:
```
examples/01_direct_vs_import_example/
├── hello_module_example.py
└── run_hello_module_example.py
```

### 🔹 File 1: `hello_module_example.py`
```python
def greet():
    print("[hello_module_example] greet() function executed")

print("[hello_module_example] This line runs always")

if __name__ == "__main__":
    print("[hello_module_example] Script is being run directly")
    greet()
```

### 🔹 File 2: `run_hello_module_example.py`
```python
import hello_module_example

print("[run_hello_module_example] This is the test driver running!")
```

### 🧪 Try running them:
- `python hello_module_example.py` → All lines run
- `python run_hello_module_example.py` → Only lines outside the `if __name__ == "__main__"` block run

---

## 🏦 Guided Exercise: Bank Manager vs Bank Worker

This scenario demonstrates a **real-world case** where `main guard` is essential.

📁 Path:
```
04_functions_exceptions/
└── main_guard/
    └── exercises/
        └── 01_bank_transaction_guard/
            ├── bank_worker.py
            └── bank_manager.py
```

### 🔹 `bank_worker.py`
- Defines a function `process_transaction()`
- Always prints a load message
- Includes a `main guard` that warns the user if run directly (this file is not meant to be executed on its own)

### 🔹 `bank_manager.py`
- Imports `bank_worker`
- Defines a function `run_daily_transaction()`
- Uses a `main guard` to ensure the transaction only runs when executed directly

### 🧪 You can test your implementation with:
```bash
python tests/04_functions_exceptions_test/main_guard_test/test_bank_manager.py
```
This test validates both the direct output and ensures the main guard properly prevents execution during import.

---

By combining theory and realistic scenarios, you’ll deeply understand when and why `if __name__ == "__main__"` is essential in Python development.
