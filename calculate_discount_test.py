from calculate_discount import calculate_discount

from datetime import date
from decimal import Decimal
import pytest

_test_data_out_of_advent = [
    pytest.param(date(2021, 11, 30), Decimal("0.01"), Decimal("0"), id="1:Date in 2021 Advent, first tier"),
    pytest.param(date(2022, 11, 25), Decimal("0.01"), Decimal("0"), id="2:Date one day before Advent, first tier"),
    pytest.param(date(2021, 12, 5), Decimal("100"), Decimal("0"), id="3:Date in 2021 Advent, Sunday"),
    pytest.param(date(2022, 11, 25), Decimal("100"), Decimal("0"), id="4:Date one day before Advent, second tier"),
    pytest.param(date(2021, 12, 4), Decimal("500"), Decimal("0"), id="5:Date in 2021 Advent, Saturday"),
    pytest.param(date(2022, 11, 25), Decimal("500"), Decimal("0"), id="6:Date one day before Advent, third tier")
]


@pytest.mark.parametrize("day,total,expected", _test_data_out_of_advent)
def test_calculate_discount_out_of_advent(day: date, total: Decimal, expected: Decimal):
    # Act
    actual = calculate_discount(day, total)
    # Assert
    assert actual == expected


_test_data_in_advent = [
    pytest.param(date(2021, 11, 30), Decimal("0.01"), Decimal("0"), id="1:Date in 2021 Advent, first tier")

]


@pytest.mark.parametrize("day,total,expected", _test_data_in_advent)
def test_calculate_discount_in_advent(day: date, total: Decimal, expected: Decimal):
    # Act
    actual = calculate_discount(day, total)
    # Assert
    assert actual == expected


_invalid_test_data = [
    pytest.param("A", Decimal("0.01"), id="99:Date in 2021 Advent, first tier")
]


@pytest.mark.parametrize("day,total", _invalid_test_data)
def test_invalid_arguments(day: date, total: Decimal):
    with pytest.raises(ValueError) as exception_info:
        calculate_discount(day, total)
    assert exception_info.type == ValueError