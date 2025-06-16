from calculator import add

# Empty string returns 0
def test_empty_string_returns_zero():
    assert add("") == 0

# Single number returns its value
def test_single_number_returns_its_value():
    assert add("1") == 1

# Two numbers comma-delimited returns their sum
def test_two_numbers_comma_delimited():
    assert add("1,2") == 3

# Multiple numbers comma-delimited returns their sum
def test_multiple_numbers_comma_delimited():
    assert add("1,2,3,4") == 10

# Newline as delimiter
def test_newline_as_delimiter():
    assert add("1\n2,3") == 6
