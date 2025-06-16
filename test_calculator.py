from calculator import add

# Empty string returns 0
def test_empty_string_returns_zero():
    assert add("") == 0

# Single number returns its value
def test_single_number_returns_its_value():
    assert add("1") == 1