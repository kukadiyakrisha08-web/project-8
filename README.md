# 🔢 NumPy Analyzer

> **A Menu-Driven NumPy Data Analysis Toolkit built with Python**

NumPy Analyzer is a console-based Python project designed to demonstrate the practical use of **NumPy arrays**, **array manipulation**, **mathematical operations**, **searching, sorting, filtering**, and **statistical analysis**.

The project provides an interactive menu-driven interface through which users can create and analyze **1D, 2D, and 3D NumPy arrays**.

---

## 📌 Project Overview

The **NumPy Analyzer** simplifies common array and data-analysis operations through an easy-to-use command-line interface.

Users can:

* Create 1D, 2D, and 3D NumPy arrays
* Access array elements using indexing
* Extract data using slicing
* Perform arithmetic operations between arrays
* Combine and split arrays
* Search for specific values
* Sort array elements
* Filter values based on conditions
* Calculate aggregate values
* Perform basic statistical analysis

This project was developed as an academic Python/NumPy project with a focus on understanding array operations and building an interactive console application.

---

## ✨ Features

### 🧩 1. Array Creation

The application supports creation of:

* **1D Arrays**
* **2D Arrays**
* **3D Arrays**

Users enter the required dimensions and values, and the program automatically converts the input into a NumPy array.

Example:

```text
Select the type of array to create:

1. 1D Array
2. 2D Array
3. 3D Array

Enter your choice: 2
```

For a 2D array:

```text
[[10 20 30]
 [40 50 60]]
```

---

### 🎯 2. Indexing

Users can access individual elements from the currently selected array.

Supported indexing includes:

* 1D → index
* 2D → row and column
* 3D → block, row, and column

Example:

```text
Enter row index: 1
Enter column index: 2

Element = 60
```

---

### ✂️ 3. Slicing

The analyzer supports extracting portions of arrays using NumPy slicing.

For a 2D array:

```text
Enter the row range (start:end): 0:2
Enter the column range (start:end): 1:3
```

Output:

```text
[[20 30]
 [50 60]]
```

The program also supports slicing for 1D and 3D arrays.

---

### ➕ 4. Mathematical Operations

The project supports element-wise operations between two arrays of the same shape:

| Operation      | NumPy Operator |
| -------------- | -------------- |
| Addition       | `+`            |
| Subtraction    | `-`            |
| Multiplication | `*`            |
| Division       | `/`            |

Example:

```text
Original Array:
[[10 20 30]
 [40 50 60]]

Second Array:
[[5 5 5]
 [5 5 5]]

Result of Addition:
[[15 25 35]
 [45 55 65]]
```

The second array is reshaped to match the original array's shape before performing the operation.

---

### 🔗 5. Combining Arrays

The application can combine arrays using NumPy's vertical stacking functionality.

Example:

```text
Original Array:
[[10 20 30]
 [40 50 60]]

Second Array:
[[1 2 3]
 [4 5 6]]

Combined Array:
[[10 20 30]
 [40 50 60]
 [ 1  2  3]
 [ 4  5  6]]
```

The current implementation uses `np.vstack()` for combining arrays.

---

### ✂️ 6. Splitting Arrays

The analyzer can split:

* 1D arrays
* 2D arrays

into multiple smaller arrays using NumPy's `array_split()`.

Example:

```text
Enter number of parts: 2
```

The resulting parts are displayed individually.

---

### 🔎 7. Search

Users can search for a particular value inside an array.

The application uses:

```python
np.where()
```

to locate matching values.

For 1D arrays, the index is displayed.

For 2D arrays, row and column positions are displayed.

For 3D arrays, the matching positions are displayed.

---

### 🔃 8. Sorting

The project supports ascending sorting using:

```python
np.sort()
```

Example:

```text
Original Array:
[[30 10 20]
 [60 40 50]]

Sorted Array:
[[10 20 30]
 [40 50 60]]
```

For 2D arrays, NumPy sorting is applied along the last axis, resulting in row-wise sorting.

---

### 🔍 9. Filtering

Users can filter values based on a condition.

For example:

```text
Show elements greater than: 30
```

The application uses NumPy boolean indexing:

```python
arr[arr > value]
```

Example output:

```text
[40 50 60]
```

---

## 📊 10. Aggregates & Statistics

The analyzer provides several useful statistical operations.

### Available Operations

| Operation          | NumPy Function |
| ------------------ | -------------- |
| Sum                | `np.sum()`     |
| Mean               | `np.mean()`    |
| Median             | `np.median()`  |
| Standard Deviation | `np.std()`     |
| Variance           | `np.var()`     |
| Minimum            | `np.min()`     |
| Maximum            | `np.max()`     |

Example:

```text
Array:
[[10 20 30]
 [40 50 60]]

Median = 35.0
```

The statistics menu allows users to repeatedly perform calculations until they choose to exit.

---

# 🖥️ Main Menu

The application provides a simple menu-driven interface:

```text
==================================================
        Welcome to the NumPy Analyzer
==================================================

1. Create a NumPy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
```

Users can select an operation by entering its corresponding number.

---

# 🛠️ Technologies Used

* 🐍 **Python**
* 🔢 **NumPy**
* 💻 **Command Line Interface (CLI)**

---

# 📂 Project Structure

A recommended GitHub repository structure is:

```text
NumPy-Analyzer/
│
├── numpy_analyzer.py
├── README.md
└── requirements.txt
```

### `numpy_analyzer.py`

Contains the complete Python source code for the NumPy Analyzer.

### `README.md`

Contains project documentation, features, installation instructions, assumptions, and usage information.

### `requirements.txt`

Contains the project's Python dependency:

```text
numpy
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd NumPy-Analyzer
```

## 2. Install NumPy

```bash
pip install numpy
```

Or, if using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 3. Run the Program

```bash
python numpy_analyzer.py
```

---

# 🚀 How to Use

After starting the program, the main menu will appear.

### Step 1 — Create an Array

Select:

```text
1. Create a NumPy Array
```

Choose the required dimension and enter the values.

### Step 2 — Select an Operation

After creating an array, users can perform operations such as:

* Indexing
* Slicing
* Mathematical calculations
* Combining
* Splitting
* Searching
* Sorting
* Filtering
* Statistical calculations

### Step 3 — Exit

Select:

```text
6. Exit
```

The program displays:

```text
Thank you for using NumPy Analyzer!
Good Bye...
```

---

# 🧪 Example

### Input

```text
Enter your choice: 1

Select the type of array to create:

1. 1D Array
2. 2D Array
3. 3D Array

Enter your choice: 2

Enter the number of rows: 2
Enter the number of columns: 3

Enter 6 elements for the array separated by space:
10 20 30 40 50 60
```

### Output

```text
Array created successfully:

[[10 20 30]
 [40 50 60]]
```

Selecting the Median option produces:

```text
Median = 35.0
```

---

# 🧠 NumPy Concepts Demonstrated

This project demonstrates practical usage of several important NumPy concepts:

* `np.array()`
* `reshape()`
* Array dimensions with `ndim`
* Array size with `size`
* Indexing
* Slicing
* Element-wise arithmetic
* `np.vstack()`
* `np.array_split()`
* `np.where()`
* `np.sort()`
* Boolean indexing
* `np.sum()`
* `np.mean()`
* `np.median()`
* `np.std()`
* `np.var()`
* `np.min()`
* `np.max()`

---

# 📝 Assumptions

The following assumptions were made while developing the project:

1. Users provide valid numeric input whenever the program requests array elements.
2. Mathematical operations use a second array having the same shape as the original array.
3. Array values are entered as integers through the console.
4. Combining arrays currently uses vertical stacking.
5. Splitting is currently supported for 1D and 2D arrays.
6. Filtering currently displays values greater than a user-provided number.
7. Sorting is performed using NumPy's default ascending order.
8. The program is designed as a console-based application and does not require a graphical interface.
9. NumPy must be installed before running the program.

---

# ⚠️ Current Scope

The current implementation focuses on the core NumPy operations required for interactive array analysis.

Some advanced requirements from the broader project specification—such as a dedicated `DataAnalytics` OOP class, private internal computation methods, class methods, static methods, dot product, matrix multiplication, descending sort, percentiles, and correlation coefficients—are **not currently implemented in this source version**.

They can be added as future enhancements rather than being claimed as completed features.

---

# 🔮 Future Enhancements

Possible future improvements include:

* [ ] Convert the application into a `DataAnalytics` class
* [ ] Add constructor-based array initialization
* [ ] Add private helper methods
* [ ] Add `@classmethod` utilities
* [ ] Add `@staticmethod` utilities
* [ ] Add dot product
* [ ] Add matrix multiplication
* [ ] Add descending sorting
* [ ] Add percentile calculation
* [ ] Add correlation coefficient calculation
* [ ] Add improved input validation
* [ ] Add division-by-zero handling
* [ ] Add support for floating-point input
* [ ] Add unit tests
* [ ] Add a graphical user interface

---

# 🎓 Academic Purpose

This project was developed for educational purposes to demonstrate:

* Python programming
* NumPy fundamentals
* Array manipulation
* Statistical calculations
* Interactive CLI development
* Problem-solving
* Basic data-analysis concepts

All project code should be maintained as original work in accordance with the academic submission requirements.

---

# 👨‍💻 Author

**krisha kukadiya**

> NumPy Analyzer — Python & NumPy Academic Project

---

# 📜 License

This project is intended primarily for educational and academic use.

If you choose to publish it publicly, add an appropriate open-source license such as MIT according to your institution's requirements.

---

## ⭐ Project Highlights

**Simple • Interactive • NumPy-Powered • Beginner-Friendly • Educational**

If you find this project useful, consider giving the repository a ⭐ on GitHub!

---

### 📌 Submission Checklist

Before submitting the project, make sure the GitHub repository contains:

* ✅ Python source code
* ✅ `README.md`
* ✅ `requirements.txt`
* ✅ Correct repository name
* ✅ Working program
* ✅ Clear project description
* ✅ Assumptions/documentation
* ✅ No copied code from unauthorized sources
