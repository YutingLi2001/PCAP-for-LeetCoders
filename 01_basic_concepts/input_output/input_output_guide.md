# Python Input & Output (I/O)

Understanding input and output is essential for building interactive Python programs. This section covers the most commonly used I/O functions in Python, especially useful for PCAP exam preparation.

---

## 🧾 Table of Contents
1. [Basic Output: `print()`](#1-basic-output-print)
2. [Formatted Output: f-strings and `format()`](#2-formatted-output-f-strings-and-format)
3. [Basic Input: `input()`](#3-basic-input-input)
4. [Type Conversion with Input](#4-type-conversion-with-input)
5. [Reading Multiple Values](#5-reading-multiple-values)
6. [Common Pitfalls](#6-common-pitfalls)

---

## 1. Basic Output: `print()`
The `print()` function is used to display output to the console.

```python
print("Hello, World!")
```
**Output:**
```
Hello, World!
```

You can print multiple values separated by commas:
```python
name = "Alice"
age = 25
print("Name:", name, "Age:", age)
```
**Output:**
```
Name: Alice Age: 25
```

By default, `print()` adds a newline at the end. You can change this using `end`:
```python
print("Loading", end="...")
print("Done")
```
**Output:**
```
Loading...Done
```

---

## 2. Formatted Output: f-strings and `format()`

### 🔹 f-strings (Python 3.6+)
```python
name = "Alice"
age = 25
print(f"{name} is {age} years old.")
```
**Output:**
```
Alice is 25 years old.
```

You can also format numbers:
```python
pi = 3.1415926
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
```
**Output:**
```
Pi rounded to 2 decimal places: 3.14
```

### 🔹 `str.format()`
```python
print("{} is {} years old.".format(name, age))
```
**Output:**
```
Alice is 25 years old.
```

You can also use numbered or named placeholders:
```python
print("{1} is {0} years old.".format(25, "Alice"))
```
**Output:**
```
Alice is 25 years old.
```

---

## 3. Basic Input: `input()`
The `input()` function reads a line from standard input and returns it as a string.

```python
name = input("Enter your name: ")
print("Hello,", name)
```
**Example Input:**
```
Bob
```
**Output:**
```
Hello, Bob
```

Another example:
```python
city = input("Which city do you live in? ")
print(f"Nice! I've heard {city} is beautiful.")
```
**Input:**
```
Vancouver
```
**Output:**
```
Nice! I've heard Vancouver is beautiful.
```

---

## 4. Type Conversion with Input
All input is read as a string. To work with numbers, you must explicitly convert types:

```python
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
```
**Example Input:**
```
24
50000.75
```
**Output:**
```
(age and salary are now usable as numeric values)
```

Converting to boolean:
```python
flag = bool(int(input("Enter 1 for True, 0 for False: ")))
print(flag)
```
**Input:**
```
1
```
**Output:**
```
True
```

---

## 5. Reading Multiple Values
Use `split()` to capture multiple values from one line:

```python
x, y = input("Enter two numbers: ").split()
x = int(x)
y = int(y)
print("Sum:", x + y)
```
**Input:**
```
10 20
```
**Output:**
```
Sum: 30
```

Using `map()` for cleaner syntax:
```python
x, y = map(int, input("Enter two numbers: ").split())
print(x * y)
```
**Input:**
```
4 5
```
**Output:**
```
20
```

---

## 6. Common Pitfalls

- ❌ Forgetting that `input()` returns a string:
  ```python
  number = input("Enter a number: ")
  print(number * 2)  # Repeats string, not math
  ```
  **Input:** `3`
  **Output:** `33`

- ✅ Correct:
  ```python
  number = int(input("Enter a number: "))
  print(number * 2)
  ```
  **Output:** `6`

- ❌ Not validating numeric input:
  ```python
  age = int(input("Enter age: "))  # May crash if input is not numeric
  ```

- ✅ Safer version with try-except (see exception handling section):
  ```python
  try:
      age = int(input("Enter age: "))
  except ValueError:
      print("Invalid number!")
  ```

---

📌 *This document is part of the `PCAP-for-LeetCoders` repository. Make sure to review and experiment with the examples to solidify your understanding.*

