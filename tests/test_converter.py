# test_converter.py
import pytest
from src.converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilometers_to_miles,
    miles_to_kilometers,
)


def test_celsius_to_fahrenheit_boiling():
    assert celsius_to_fahrenheit(100) == 212.0


def test_celsius_to_fahrenheit_freezing():
    assert celsius_to_fahrenheit(0) == 32.0


def test_fahrenheit_to_celsius_body_temp():
    assert fahrenheit_to_celsius(98.6) == 37.0


def test_celsius_to_fahrenheit_type_error():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("hot")


def test_kilometers_to_miles_basic():
    assert kilometers_to_miles(1) == 0.6214


def test_kilometers_to_miles_negative_raises():
    with pytest.raises(ValueError):
        kilometers_to_miles(-5)


def test_miles_to_kilometers_basic():
    assert miles_to_kilometers(1) == 1.6093


def test_miles_to_kilometers_type_error():
    with pytest.raises(TypeError):
        miles_to_kilometers("far")
