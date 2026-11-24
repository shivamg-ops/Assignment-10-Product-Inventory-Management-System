"""Product Inventory Management System.

Provides core functions for product price calculations, discounts,
stock checks, input validation, and detailed logging.
"""

from __future__ import annotations

import logging

# Configure logging
LOG_FILE = "application.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def calculate_total_price(price: float, quantity: int) -> float:
    """Calculate and return the total price based on unit price and quantity.

    Args:
        price: Unit price of the product (must be non-negative number).
        quantity: Quantity of the product (must be non-negative integer).

    Returns:
        Total price as a float.

    Raises:
        TypeError: If price or quantity is of invalid type.
        ValueError: If price < 0 or quantity < 0.
    """
    logger.info(
        "calculate_total_price called with price=%s, quantity=%s", price, quantity
    )

    if isinstance(price, bool) or not isinstance(price, (int, float)):
        logger.error("Invalid type for price: %s", type(price).__name__)
        raise TypeError("Price must be a valid number (int or float).")

    if isinstance(quantity, bool) or not isinstance(quantity, int):
        logger.error("Invalid type for quantity: %s", type(quantity).__name__)
        raise TypeError("Quantity must be an integer.")

    if price < 0:
        logger.error("Negative price encountered: %s", price)
        raise ValueError("Price cannot be negative.")

    if quantity < 0:
        logger.error("Negative quantity encountered: %s", quantity)
        raise ValueError("Quantity cannot be negative.")

    total = round(float(price * quantity), 2)
    logger.info("Successfully calculated total price: %s", total)
    return total


def apply_discount(total: float, discount_percent: float) -> float:
    """Calculate and return the final discounted amount.

    Args:
        total: Original total amount (must be non-negative number).
        discount_percent: Discount percentage between 0 and 100 inclusive.

    Returns:
        Discounted total price as a float.

    Raises:
        TypeError: If total or discount_percent is of invalid type.
        ValueError: If total < 0 or discount_percent not in [0, 100].
    """
    logger.info(
        "apply_discount called with total=%s, discount_percent=%s",
        total,
        discount_percent,
    )

    if isinstance(total, bool) or not isinstance(total, (int, float)):
        logger.error("Invalid type for total: %s", type(total).__name__)
        raise TypeError("Total must be a valid number (int or float).")

    if isinstance(discount_percent, bool) or not isinstance(
        discount_percent, (int, float)
    ):
        logger.error(
            "Invalid type for discount_percent: %s", type(discount_percent).__name__
        )
        raise TypeError("Discount percentage must be a valid number.")

    if total < 0:
        logger.error("Negative total encountered: %s", total)
        raise ValueError("Total amount cannot be negative.")

    if not (0 <= discount_percent <= 100):
        logger.error("Discount percent out of bounds (0-100): %s", discount_percent)
        raise ValueError("Discount percentage must be between 0 and 100.")

    discounted_amount = round(float(total * (1 - discount_percent / 100.0)), 2)
    logger.info("Successfully applied discount: final amount=%s", discounted_amount)
    return discounted_amount


def check_stock(available_stock: int, requested_quantity: int) -> bool:
    """Check whether the requested quantity can be fulfilled by available stock.

    Args:
        available_stock: Available inventory stock count (non-negative integer).
        requested_quantity: Requested item count (positive integer).

    Returns:
        True if requested_quantity <= available_stock, False otherwise.

    Raises:
        TypeError: If available_stock or requested_quantity is not an integer.
        ValueError: If available_stock < 0 or requested_quantity <= 0.
    """
    logger.info(
        "check_stock called with available_stock=%s, requested_quantity=%s",
        available_stock,
        requested_quantity,
    )

    if isinstance(available_stock, bool) or not isinstance(available_stock, int):
        logger.error(
            "Invalid type for available_stock: %s", type(available_stock).__name__
        )
        raise TypeError("Available stock must be an integer.")

    if isinstance(requested_quantity, bool) or not isinstance(requested_quantity, int):
        logger.error(
            "Invalid type for requested_quantity: %s", type(requested_quantity).__name__
        )
        raise TypeError("Requested quantity must be an integer.")

    if available_stock < 0:
        logger.error("Negative available_stock encountered: %s", available_stock)
        raise ValueError("Available stock cannot be negative.")

    if requested_quantity <= 0:
        logger.error("Non-positive requested_quantity: %s", requested_quantity)
        raise ValueError("Requested quantity must be greater than zero.")

    if requested_quantity <= available_stock:
        logger.info(
            "Stock check PASSED: requested %s is available (stock: %s)",
            requested_quantity,
            available_stock,
        )
        return True

    logger.warning(
        "Stock check FAILED: requested %s exceeds available stock %s",
        requested_quantity,
        available_stock,
    )
    return False


def main() -> None:
    """Demonstrate sample usage of the inventory system."""
    print("=== Product Inventory Management System ===")
    try:
        price = 49.99
        qty = 3
        total = calculate_total_price(price, qty)
        print(f"Total price for {qty} items at ${price}: ${total:.2f}")

        discount = 10
        final_price = apply_discount(total, discount)
        print(f"Price after {discount}% discount: ${final_price:.2f}")

        stock = 25
        order_qty = 5
        can_fulfill = check_stock(stock, order_qty)
        print(
            f"Can fulfill order of {order_qty} items (Stock: {stock})? {'Yes' if can_fulfill else 'No'}"
        )
    except Exception:
        logger.exception("An unexpected error occurred in main execution")
        print("An error occurred. Check application.log for details.")


if __name__ == "__main__":
    main()
