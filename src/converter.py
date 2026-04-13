# converter.py
# Unit conversion module


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    if not isinstance(c, (int, float)):
        raise TypeError("temperature must be a number")
    return round((c * 9 / 5) + 32, 2)


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    if not isinstance(f, (int, float)):
        raise TypeError("temperature must be a number")
    return round((f - 32) * 5 / 9, 2)


def kilometers_to_miles(km):
    """Convert kilometers to miles."""
    if not isinstance(km, (int, float)):
        raise TypeError("distance must be a number")
    if km < 0:
        raise ValueError("distance cannot be negative")
    return round(km * 0.621371, 4)


def miles_to_kilometers(mi):
    """Convert miles to kilometers."""
    if not isinstance(mi, (int, float)):
        raise TypeError("distance must be a number")
    if mi < 0:
        raise ValueError("distance cannot be negative")
    return round(mi * 1.60934, 4)
