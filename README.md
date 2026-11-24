# Product Inventory Management System

A robust, production-grade Python application developed for **Assignment 10** to manage product inventories, calculate totals, handle percentage discounts, evaluate stock availability, and maintain structured logging and test coverage.

---

## 📋 Features Implemented

1. **Total Price Calculation (`calculate_total_price`)**:
   - Calculates product total price based on unit price and quantity.
   - Strictly validates input types (`int` / `float` for price, `int` for quantity, excluding booleans).
   - Raises `ValueError` for negative prices or quantities.
   - Automatically logs calculations and errors.

2. **Discount Calculation (`apply_discount`)**:
   - Computes the discounted final price using a percentage discount.
   - Enforces valid boundaries: discount must be between `0%` and `100%`.
   - Rejects negative total amounts and non-numeric inputs with clear exceptions.
   - Automatically logs operations.

3. **Stock Availability Checking (`check_stock`)**:
   - Verifies whether requested product quantity can be fulfilled by current inventory.
   - Returns boolean `True` if available stock is sufficient, `False` otherwise.
   - Raises `ValueError` for invalid requested quantities ($\le 0$) or negative available stocks.
   - Logs successes, warnings when stock is insufficient, and errors.

4. **Structured Logging**:
   - Integrated with Python's standard `logging` module.
   - Writes timestamped, level-tagged records (`INFO`, `WARNING`, `ERROR`) to `application.log`.

5. **Unit Testing (`pytest`)**:
   - 16 comprehensive unit tests covering:
     - Standard valid inputs
     - Boundary conditions ($0$ price, $0$ quantity, $0\%$ and $100\%$ discount, exact stock availability)
     - Invalid inputs and type errors verifying exception raises (`TypeError`, `ValueError`)

6. **Code Quality & Formatting (`Ruff`)**:
   - Linted and formatted according to modern Python standards with **Ruff**.
   - Zero lint errors and formatting violations.

---

## 📁 Project Structure

```text
product-inventory-management/
├── .gitignore             # Configured to ignore .venv, caches, and OS artifacts
├── README.md              # Project documentation and guide
├── application.log        # Generated runtime log file
├── inventory.py           # Core system implementation & CLI demo
└── test_inventory.py      # Full pytest test suite
```

---

## 💻 macOS Setup Instructions

### 1. Prerequisites
Ensure you have Python 3.10+ installed on macOS. Check via terminal:
```bash
python3 --version
```

### 2. Clone the Repository (or navigate to directory)
```bash
git clone https://github.com/<your-username>/product-inventory-management.git
cd product-inventory-management
```

### 3. Create and Activate Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
Install `pytest` and `ruff`:
```bash
pip install pytest ruff
```

---

## 🚀 Execution Instructions

Run the main application script:
```bash
python3 inventory.py
```

### Expected Output
```text
=== Product Inventory Management System ===
Total price for 3 items at $49.99: $149.97
Price after 10% discount: $134.97
Can fulfill order of 5 items (Stock: 25)? Yes
```

Check the log file created:
```bash
cat application.log
```

---

## 🧪 Testing Instructions

Run the test suite with `pytest`:
```bash
pytest -v
```

All 16 test cases should pass:
```text
test_inventory.py::TestCalculateTotalPrice::test_valid_price_and_quantity PASSED
test_inventory.py::TestCalculateTotalPrice::test_zero_quantity_and_zero_price_boundary PASSED
test_inventory.py::TestCalculateTotalPrice::test_negative_price_raises_value_error PASSED
test_inventory.py::TestCalculateTotalPrice::test_negative_quantity_raises_value_error PASSED
test_inventory.py::TestCalculateTotalPrice::test_invalid_types_raise_type_error PASSED
test_inventory.py::TestApplyDiscount::test_valid_discount PASSED
test_inventory.py::TestApplyDiscount::test_boundary_discounts PASSED
test_inventory.py::TestApplyDiscount::test_discount_out_of_range_raises_value_error PASSED
test_inventory.py::TestApplyDiscount::test_negative_total_raises_value_error PASSED
test_inventory.py::TestApplyDiscount::test_invalid_types_raise_type_error PASSED
test_inventory.py::TestCheckStock::test_stock_sufficient PASSED
test_inventory.py::TestCheckStock::test_stock_exact_boundary PASSED
test_inventory.py::TestCheckStock::test_stock_insufficient PASSED
test_inventory.py::TestCheckStock::test_invalid_quantity_raises_value_error PASSED
test_inventory.py::TestCheckStock::test_negative_stock_raises_value_error PASSED
test_inventory.py::TestCheckStock::test_invalid_types_raise_type_error PASSED
```

---

## 🔍 Code Quality & Linting (Ruff)

### Run Ruff Linter
```bash
ruff check .
```
Expected output:
```text
All checks passed!
```

### Run Ruff Formatter Check
```bash
ruff format --check .
```
Expected output:
```text
2 files already formatted
```

---

## 📸 Screenshots for Submission

You can capture screenshots of your terminal running:
1. **Pytest execution:**
   ```bash
   pytest -v
   ```
2. **Ruff checks:**
   ```bash
   ruff check . && ruff format --check .
   ```

---

## 📦 Git & GitHub Submission Checklist

Follow these commands to push your project to GitHub:

1. Initialize git and configure main branch:
   ```bash
   git init
   git branch -M main
   ```

2. Add all files (verifying `.venv/` is excluded via `.gitignore`):
   ```bash
   git status
   git add .
   git commit -m "Complete Assignment 10 Product Inventory Management System"
   ```

3. Create repository on GitHub named `product-inventory-management` and push:
   ```bash
   git remote add origin https://github.com/<your-username>/product-inventory-management.git
   git push -u origin main
   ```
