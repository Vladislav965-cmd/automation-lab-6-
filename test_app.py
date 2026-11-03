import pytest

from app import order_total


def test_without_discount():
    assert order_total(100, 3) == 300


def test_with_discount():
    assert order_total(250, 4, 10) == 900


def test_zero_quantity():
    assert order_total(99.9, 0) == 0


def test_negative_price():
    with pytest.raises(ValueError):
        order_total(-1, 2)


def test_wrong_discount():
    with pytest.raises(ValueError):
        order_total(100, 1, 150)
