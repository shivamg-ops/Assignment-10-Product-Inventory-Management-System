import pytest

from inventory import apply_discount, calculate_total_price, check_stock


# Tests for calculate_total_price
def test_calculate_total_price_valid():
    assert calculate_total_price(50, 2) == 100
    assert calculate_total_price(10.5, 4) == 42.0


def test_calculate_total_price_zero():
    assert calculate_total_price(0, 5) == 0
    assert calculate_total_price(10, 0) == 0


def test_calculate_total_price_negative():
    with pytest.raises(ValueError):
        calculate_total_price(-10, 2)
    with pytest.raises(ValueError):
        calculate_total_price(10, -2)


def test_calculate_total_price_invalid_type():
    with pytest.raises(TypeError):
        calculate_total_price("10", 2)
    with pytest.raises(TypeError):
        calculate_total_price(10, "2")


# Tests for apply_discount
def test_apply_discount_valid():
    assert apply_discount(100, 10) == 90.0
    assert apply_discount(200, 25) == 150.0


def test_apply_discount_boundary():
    assert apply_discount(100, 0) == 100.0
    assert apply_discount(100, 100) == 0.0


def test_apply_discount_invalid_percentage():
    with pytest.raises(ValueError):
        apply_discount(100, -5)
    with pytest.raises(ValueError):
        apply_discount(100, 105)


def test_apply_discount_negative_total():
    with pytest.raises(ValueError):
        apply_discount(-50, 10)


# Tests for check_stock
def test_check_stock_available():
    assert check_stock(10, 5) is True
    assert check_stock(5, 5) is True


def test_check_stock_unavailable():
    assert check_stock(5, 10) is False
    assert check_stock(0, 1) is False


def test_check_stock_invalid_quantity():
    with pytest.raises(ValueError):
        check_stock(10, 0)
    with pytest.raises(ValueError):
        check_stock(10, -3)


def test_check_stock_invalid_type():
    with pytest.raises(TypeError):
        check_stock("10", 5)
    with pytest.raises(TypeError):
        check_stock(10, 2.5)
