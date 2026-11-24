# Assignment 10 – Product Inventory Management System

A Python-based Product Inventory Management System designed to handle core inventory calculations, strict input validation, exception handling, automated unit testing, logging, and code quality formatting.

---

## 🏗️ System Architecture & End-to-End Flow

### 1. High-Level Architecture
```mermaid
flowchart TD
    subgraph Client / User Layer
        CLI[Main Execution / Client Input]
        Tests[Pytest Test Suite]
    end

    subgraph Business Logic Layer [inventory.py]
        direction TB
        CalcTotal["calculate_total_price(price, quantity)"]
        ApplyDisc["apply_discount(total, discount_percent)"]
        StockCheck["check_stock(available_stock, requested_quantity)"]
    end

    subgraph Validation & Exception Layer
        TypeCheck{Type Validation}
        RangeCheck{Value / Boundary Validation}
        TypeErr[Raise TypeError]
        ValErr[Raise ValueError]
    end

    subgraph Output & Observability Layer
        LogModule[(Python Logging)]
        AppLog[application.log]
        Result[Valid Output / Return Value]
    end

    CLI --> CalcTotal & ApplyDisc & StockCheck
    Tests --> CalcTotal & ApplyDisc & StockCheck

    CalcTotal --> TypeCheck
    ApplyDisc --> TypeCheck
    StockCheck --> TypeCheck

    TypeCheck -- Invalid Type --> TypeErr --> LogModule
    TypeCheck -- Valid Type --> RangeCheck

    RangeCheck -- Invalid Value --> ValErr --> LogModule
    RangeCheck -- Valid Value --> Result --> LogModule

    LogModule --> AppLog
```

---

### 2. End-to-End Workflow Diagram
```mermaid
sequenceDiagram
    autonumber
    actor User as User / Pytest Runner
    participant Core as inventory.py
    participant Val as Input Validator
    participant Log as Logger (application.log)

    User->>Core: Request Operation (e.g. calculate_total_price)
    Core->>Val: Check data types (int/float, non-bool)
    alt Invalid Data Type
        Val-->>Core: Type mismatch detected
        Core->>Log: log.error("Invalid type...")
        Core-->>User: Raise TypeError
    else Valid Data Type
        Core->>Val: Check values (non-negative, range limits)
        alt Invalid Value Range
            Val-->>Core: Value out of bounds
            Core->>Log: log.error("Negative/Invalid value...")
            Core-->>User: Raise ValueError
        else Valid Value Range
            Core->>Core: Compute formula (Price / Discount / Stock)
            Core->>Log: log.info("Operation successful...")
            Core-->>User: Return computed result
        end
    end
```

---

## 📋 Features Implemented

1. **Total Price Calculation (`calculate_total_price`)**:
   - Computes total cost based on price and quantity.
   - Validates numeric inputs and rejects negative values or boolean types.
   - Logs operations and calculation outcomes.

2. **Discount Calculation (`apply_discount`)**:
   - Calculates discounted amount based on percentage (0% to 100%).
   - Validates that discount falls strictly within standard percentage limits.
   - Raises appropriate exceptions on negative totals or out-of-range discounts.

3. **Stock Availability Checking (`check_stock`)**:
   - Checks if inventory can fulfill requested quantity.
   - Returns boolean (`True` / `False`).
   - Ensures requested quantity is positive ($> 0$) and available stock is non-negative ($\ge 0$).
   - Records warnings when stock is insufficient.

4. **Logging System**:
   - Uses standard Python `logging`.
   - Records timestamps, log levels (`INFO`, `WARNING`, `ERROR`), and detailed messages to `application.log`.

5. **Testing & Code Quality**:
   - 12 comprehensive unit tests using `pytest` covering normal inputs, edge boundaries, and exceptions.
   - Linted and auto-formatted using `Ruff` with zero warnings.

---

## 📸 Test Execution & Linting Screenshots

### 1. Pytest Test Suite Execution
All unit tests executed and passed successfully across all functions:
![Pytest Execution](sreenshots/1.%20Pytest.png)

### 2. Ruff Quality Checks & Formatting
Ruff code analysis and format checks passing cleanly:
![Ruff Checks](sreenshots/2.%20Ruff%20Checks.png)

![Ruff Check Verification](sreenshots/2.1.%20ruff%20check.png)

---

## 📁 Project Structure

```text
product-inventory-management/
├── .gitignore             # Configured to ignore .venv, cache, and OS artifacts
├── README.md              # Project documentation, diagrams, and setup instructions
├── application.log        # Generated runtime log file
├── inventory.py           # Core implementation logic
├── test_inventory.py      # Pytest test suite
└── sreenshots/            # Execution and verification screenshots
    ├── 1. Pytest.png
    ├── 2. Ruff Checks.png
    └── 2.1. ruff check.png
```

---

## 💻 macOS Setup Instructions

### 1. Prerequisites
Ensure Python 3.10 or higher is installed:
```bash
python3 --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/shivamg-ops/Assignment-10-Product-Inventory-Management-System.git
cd Assignment-10-Product-Inventory-Management-System
```

### 3. Create and Activate Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install pytest ruff
```

---

## 🚀 Execution Instructions

Run the main application:
```bash
python3 inventory.py
```

### Expected Output
```text
Total Price: 150.0
After Discount: 135.0
Stock Available: True
```

Inspect generated logs:
```bash
cat application.log
```

---

## 🧪 Testing Instructions

Run the pytest test suite:
```bash
pytest -v
```

### Test Coverage Summary
- `calculate_total_price`: Valid inputs, zero value boundary, negative value errors, invalid types.
- `apply_discount`: Valid discounts, 0% and 100% boundaries, out-of-range percentage, negative total errors.
- `check_stock`: Available stock, insufficient stock, non-positive requested quantity, invalid types.

---

## 🔍 Code Quality Instructions (Ruff)

Check linting:
```bash
ruff check .
```

Check code formatting:
```bash
ruff format --check .
```
