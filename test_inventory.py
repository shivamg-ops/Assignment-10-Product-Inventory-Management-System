"""Unit tests for the Product Inventory Management System.

Covers valid inputs, boundary conditions, and invalid inputs/exceptions
for calculate_total_price, apply_discount, and check_stock.
"""

import pytest

from inventory import apply_discount, calculate_total_price, check_stock


# ============================================================================
# Tests for calculate_total_price
# ============================================================================
class TestCalculateTotalPrice:
    """Tests for calculate_total_price."""

    def test_valid_price_and_quantity(self):
        """Test with typical valid inputs."""
        assert calculate_total_price(10.50, 4) == 42.0
        assert calculate_total_price(100, 2) == 200.0

    def test_zero_quantity_and_zero_price_boundary(self):
        """Test boundary conditions with zero values."""
        assert calculate_total_price(0, 5) == 0.0
        assert calculate_total_price(15.99, 0) == 0.0
        assert calculate_total_price(0, 0) == 0.0

    def test_negative_price_raises_value_error(self):
        """Test that negative price raises ValueError."""
        with pytest.raises(ValueError, match="Price cannot be negative."):
            calculate_total_price(-10.0, 2)

    def test_negative_quantity_raises_value_error(self):
        """Test that negative quantity raises ValueError."""
        with pytest.raises(ValueError, match="Quantity cannot be negative."):
            calculate_total_price(15.0, -1)

    def test_invalid_types_raise_type_error(self):
        """Test invalid types for price and quantity."""
        with pytest.raises(TypeError, match="Price must be a valid number"):
            calculate_total_price("50", 2)  # type: ignore[arg-type]

        with pytest.raises(TypeError, match="Quantity must be an integer"):
            calculate_total_price(50, 2.5)  # type: ignore[arg-type]

        with pytest.raises(TypeError, match="Price must be a valid number"):
            calculate_total_price(True, 2)  # type: ignore[arg-type]


# ============================================================================
# Tests for apply_discount
# ============================================================================
class TestApplyDiscount:
    """Tests for apply_discount."""

    def test_valid_discount(self):
        """Test valid percentage discount application."""
        assert apply_discount(100.0, 20) == 80.0
        assert apply_discount(250.0, 15.5) == 211.25

    def test_boundary_discounts(self):
        """Test boundaries at 0% and 100% discount."""
        assert apply_discount(150.0, 0) == 150.0
        assert apply_discount(150.0, 100) == 0.0
        assert apply_discount(0.0, 50) == 0.0

    def test_discount_out_of_range_raises_value_error(self):
        """Test discount below 0 or above 100 raises ValueError."""
        with pytest.raises(
            ValueError, match="Discount percentage must be between 0 and 100."
        ):
            apply_discount(100.0, -5)

        with pytest.raises(
            ValueError, match="Discount percentage must be between 0 and 100."
        ):
            apply_discount(100.0, 105)

    def test_negative_total_raises_value_error(self):
        """Test that negative total raises ValueError."""
        with pytest.raises(ValueError, match="Total amount cannot be negative."):
            apply_discount(-50.0, 10)

    def test_invalid_types_raise_type_error(self):
        """Test invalid types for total and discount_percent."""
        with pytest.raises(TypeError, match="Total must be a valid number"):
            apply_discount("100", 10)  # type: ignore[arg-type]

        with pytest.raises(
            TypeError, match="Discount percentage must be a valid number"
        ):
            apply_discount(100, "10%")  # type: ignore[arg-type]


# ============================================================================
# Tests for check_stock
# ============================================================================
class TestCheckStock:
    """Tests for check_stock."""

    def test_stock_sufficient(self):
        """Test when requested quantity is less than available stock."""
        assert check_stock(available_stock=50, requested_quantity=10) is True

    def test_stock_exact_boundary(self):
        """Test when requested quantity exactly equals available stock."""
        assert check_stock(available_stock=20, requested_quantity=20) is True

    def test_stock_insufficient(self):
        """Test when requested quantity exceeds available stock."""
        assert check_stock(available_stock=5, requested_quantity=10) is False
        assert check_stock(available_stock=0, requested_quantity=1) is False

    def test_invalid_quantity_raises_value_error(self):
        """Test non-positive quantity raises ValueError."""
        with pytest.raises(
            ValueError, match="Requested quantity must be greater than zero."
        ):
            check_stock(available_stock=10, requested_quantity=0)

        with pytest.raises(
            ValueError, match="Requested quantity must be greater than zero."
        ):
            check_stock(available_stock=10, requested_quantity=-5)

    def test_negative_stock_raises_value_error(self):
        """Test negative available stock raises ValueError."""
        with pytest.raises(ValueError, match="Available stock cannot be negative."):
            check_stock(available_stock=-2, requested_quantity=5)

    def test_invalid_types_raise_type_error(self):
        """Test that non-integer types raise TypeError."""
        with pytest.raises(TypeError, match="Available stock must be an integer"):
            check_stock(10.5, 5)  # type: ignore[arg-type]

        with pytest.raises(TypeError, match="Requested quantity must be an integer"):
            check_stock(10, 2.5)  # type: ignore[arg-type]
