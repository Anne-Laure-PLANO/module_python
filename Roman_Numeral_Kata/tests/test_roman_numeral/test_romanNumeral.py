import pytest

from roman_numeral.romanNumeral import convertNumber, isValidNumber


@pytest.mark.parametrize(
    "number,expected",
    [(1, "I"), (5, "V"), (10, "X"), (50, "L"), (666, "DCLXVI"), (14, "XIV")],
)
def test_convert(number, expected):
    result = convertNumber(number)
    assert result == expected


def test_isValidNumber():
    result = isValidNumber("12")
    assert result == True


def test_isValidNumber_false():
    result = isValidNumber("bla")
    assert result == False


def test_isValidNumber_carSpe():
    result = isValidNumber("&")
    assert result == False


def test_isValidNumber_intEtStr():
    result = isValidNumber("12D")
    assert result == False
