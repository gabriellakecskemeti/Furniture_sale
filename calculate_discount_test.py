from calculate_discount import calculate_discount

from datetime import date
from decimal import Decimal
import pytest

_test_data_before_advent = [
    pytest.param(date(2021, 11, 30), Decimal("0.01"), Decimal("0"), id="1:Date in 2021 Advent, first tier")
]


@pytest.mark.parametrize("day,total,expected", _test_data_before_advent)
def test_calculate_discount_before_advent(day: date, total: Decimal, expected: Decimal):
    # Act
    actual = calculate_discount(day, total)
    # Assert
    assert actual == expected
