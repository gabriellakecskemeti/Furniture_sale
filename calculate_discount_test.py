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
    pytest.param(date(2022, 11, 25), Decimal("500"), Decimal("0"), id="6:Date one day before Advent, third tier"),
    pytest.param(date(2022, 12, 27), Decimal("90"), Decimal("0"), id="40:After advent, first tier"),
    pytest.param(date(2023, 1, 7), Decimal("400"), Decimal("0"), id="41:After advent, second tier"),
    pytest.param(date(2022, 12, 29), Decimal("500"), Decimal("0"), id="42:After advent, third tier")
]


@pytest.mark.parametrize("day,total,expected", _test_data_out_of_advent)
def test_calculate_discount_out_of_advent(day: date, total: Decimal, expected: Decimal):
    # Act
    actual = calculate_discount(day, total)
    # Assert
    assert actual == expected


_test_data_in_advent = [
    pytest.param(date(2022, 11, 28), Decimal("0.01"), Decimal("0.05"), id="7:Week1, BV1,first tier"),
    pytest.param(date(2022, 12, 2), Decimal("99.99"), Decimal("0.05"), id="8:Week1, BV2, first tier"),
    pytest.param(date(2022, 12, 1), Decimal("90"), Decimal("0.05"), id="9:Week1, EP, first tier"),
    pytest.param(date(2022, 11, 28), Decimal("100"), Decimal("0.1"), id="10:Week1, BV1, second tier"),
    pytest.param(date(2022, 12, 2), Decimal("499.999999"), Decimal("0.1"), id="11:Week1, BV2, second tier"),
    pytest.param(date(2022, 11, 30), Decimal("400"), Decimal("0.1"), id="12:Week1, EP, second tier"),
    pytest.param(date(2022, 11, 28), Decimal("500"), Decimal("0.2"), id="13:Week1, BV1, third tier"),
    pytest.param(date(2022, 12, 2), Decimal("999999.99"), Decimal("0.2"), id="14:Week1, BV2, third tier"),
    pytest.param(date(2022, 11, 30), Decimal("10000"), Decimal("0.2"), id="15:Week1, EP, third tier"),
    pytest.param(date(2022, 12, 5), Decimal("0.01"), Decimal("0.05"), id="16:Week2, BV1,first tier"),
    pytest.param(date(2022, 12, 7), Decimal("99.99"), Decimal("0.05"), id="17:Week2, BV2, first tier"),
    pytest.param(date(2022, 12, 6), Decimal("90"), Decimal("0.05"), id="18:Week2, EP, first tier"),
    pytest.param(date(2022, 12, 5), Decimal("100"), Decimal("0.1"), id="19:Week2, BV1, second tier"),
    pytest.param(date(2022, 12, 7), Decimal("499.999999"), Decimal("0.1"), id="20:Week2, BV2, second tier,truncation"),
    pytest.param(date(2022, 12, 6), Decimal("400"), Decimal("0.1"), id="21:Week2, EP, second tier"),
    pytest.param(date(2022, 12, 5), Decimal("500"), Decimal("0.2"), id="22:Week2, BV1, third tier"),
    pytest.param(date(2022, 12, 7), Decimal("10000.00"), Decimal("0.2"), id="23:Week2, BV2, third tier"),
    pytest.param(date(2022, 12, 9), Decimal("99.99"), Decimal("0.05"), id="24:Week2, EP,first tier"),
    pytest.param(date(2022, 12, 9), Decimal("100"), Decimal("0.1"), id="25:Week2, EP, second tier"),
    pytest.param(date(2022, 12, 9), Decimal("1000"), Decimal("0.2"), id="26:Week2, EP, third tier"),
    pytest.param(date(2022, 12, 12), Decimal("99.99"), Decimal("0.05"), id="27:Week3, BV1,first tier"),
    pytest.param(date(2022, 12, 16), Decimal("100"), Decimal("0.1"), id="28:Week3, BV2, second tier"),
    pytest.param(date(2022, 12, 13), Decimal("1000"), Decimal("0.2"), id="29:Week3, EP, third tier"),
    pytest.param(date(2022, 12, 19), Decimal("0.01"), Decimal("0.05"), id="30:Week4, BV1,first tier"),
    pytest.param(date(2022, 12, 23), Decimal("499.999999"), Decimal("0.1"), id="31:Week4, BV2, second tier, truncation"),
    pytest.param(date(2022, 12, 21), Decimal("1000"), Decimal("0.2"), id="32:Week4, EP, third tier")
]


@pytest.mark.parametrize("day,total,expected", _test_data_in_advent)
def test_calculate_discount_in_advent(day: date, total: Decimal, expected: Decimal):
    # Act
    actual = calculate_discount(day, total)
    # Assert
    assert actual == expected


_test_data_in_advent_saturday = [
    pytest.param(date(2022, 11, 26), Decimal("99.99"), Decimal("0.15"), id="33:Saturday1, first tier"),
    pytest.param(date(2022, 11, 26), Decimal("100"), Decimal("0.19"), id="34:Saturday1, second tier"),
    pytest.param(date(2022, 11, 26), Decimal("1000"), Decimal("0.28"), id="35:Saturday1, third tier"),
    pytest.param(date(2022, 12, 3), Decimal("99.99"), Decimal("0.15"), id="36:Saturday1, first tier"),
    pytest.param(date(2022, 12, 10), Decimal("499.999999"), Decimal("0.19"), id="37:Saturday1, second tier,truncation"),
    pytest.param(date(2022, 12, 17), Decimal("1000"), Decimal("0.28"), id="38:Saturday1, third tier"),
    pytest.param(date(2022, 12, 24), Decimal("1000"), Decimal("0.28"), id="39:Saturday1, third tier")
]


@pytest.mark.parametrize("day,total,expected", _test_data_in_advent_saturday)
def test_calculate_discount_in_advent_saturday(day: date, total: Decimal, expected: Decimal):
    # Act
    actual = calculate_discount(day, total)
    # Assert
    assert actual == expected


_invalid_test_data = [
    pytest.param(date(2022, 11, 27), Decimal("100"), id="43:not allowed date"),
    pytest.param(date(2022, 12, 4), Decimal("100"), id="44:not allowed date"),
    pytest.param(date(2022, 12, 8), Decimal("100"), id="45:not allowed date"),
    pytest.param(date(2022, 12, 11), Decimal("100"), id="46:not allowed date"),
    pytest.param(date(2022, 12, 18), Decimal("100"), id="47:not allowed date"),
    pytest.param(date(2022, 12, 25), Decimal("100"), id="48:not allowed date"),
    pytest.param(date(2022, 12, 26), Decimal("100"), id="49:not allowed date"),
    pytest.param("9999999999.12.6", Decimal("100"), id="50:not a type of date, wrong year"),
    pytest.param("2022.12.88", Decimal("100"), id="51:not a type of date, wrong day"),
    pytest.param("2022.18.8", Decimal("100"), id="52:not a type of date, wrong month"),
    pytest.param("A", Decimal("100"), id="53:not a type of date, character"),
    pytest.param(date(2022, 12, 17), Decimal("-10000"), id="54: total below 0 is not allowed"),
    pytest.param(date(2022, 12, 19), Decimal("0.00"), id="55: total = 0 is not allowed"),
    pytest.param(date(2022, 12, 20), 10.1234567, id="56: total is type of float"),
    pytest.param(date(2022, 12, 22), "x", id="57: total is a character value")
]


@pytest.mark.parametrize("day,total", _invalid_test_data)
def test_invalid_arguments(day: date, total: Decimal):
    with pytest.raises(ValueError) as exception_info:
        calculate_discount(day, total)
    assert exception_info.type == ValueError
