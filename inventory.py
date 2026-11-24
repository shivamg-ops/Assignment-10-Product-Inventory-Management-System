import logging

logging.basicConfig(
    filename="application.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def calculate_total_price(price, quantity):
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        logger.error("Invalid price type")
        raise TypeError("Price must be a number")
    if not isinstance(quantity, int) or isinstance(quantity, bool):
        logger.error("Invalid quantity type")
        raise TypeError("Quantity must be an integer")
    if price < 0:
        logger.error("Negative price: %s", price)
        raise ValueError("Price cannot be negative")
    if quantity < 0:
        logger.error("Negative quantity: %s", quantity)
        raise ValueError("Quantity cannot be negative")

    total = price * quantity
    logger.info("Total price calculated: %s", total)
    return total


def apply_discount(total, discount_percent):
    if not isinstance(total, (int, float)) or isinstance(total, bool):
        logger.error("Invalid total type")
        raise TypeError("Total must be a number")
    if not isinstance(discount_percent, (int, float)) or isinstance(
        discount_percent, bool
    ):
        logger.error("Invalid discount type")
        raise TypeError("Discount must be a number")
    if total < 0:
        logger.error("Negative total: %s", total)
        raise ValueError("Total cannot be negative")
    if discount_percent < 0 or discount_percent > 100:
        logger.error("Invalid discount percentage: %s", discount_percent)
        raise ValueError("Discount must be between 0 and 100")

    discount_amount = (total * discount_percent) / 100
    final_price = total - discount_amount
    logger.info("Discount applied. Final price: %s", final_price)
    return final_price


def check_stock(available_stock, requested_quantity):
    if not isinstance(available_stock, int) or isinstance(available_stock, bool):
        logger.error("Invalid available stock type")
        raise TypeError("Available stock must be an integer")
    if not isinstance(requested_quantity, int) or isinstance(requested_quantity, bool):
        logger.error("Invalid requested quantity type")
        raise TypeError("Requested quantity must be an integer")
    if available_stock < 0:
        logger.error("Negative stock: %s", available_stock)
        raise ValueError("Available stock cannot be negative")
    if requested_quantity <= 0:
        logger.error("Invalid requested quantity: %s", requested_quantity)
        raise ValueError("Requested quantity must be positive")

    if requested_quantity <= available_stock:
        logger.info("Stock check passed for quantity: %s", requested_quantity)
        return True
    else:
        logger.warning("Insufficient stock for requested: %s", requested_quantity)
        return False


if __name__ == "__main__":
    p = 50.0
    q = 3
    total = calculate_total_price(p, q)
    print("Total Price:", total)

    discounted = apply_discount(total, 10)
    print("After Discount:", discounted)

    in_stock = check_stock(10, q)
    print("Stock Available:", in_stock)
