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

# Custom delimiter support
def test_custom_delimiter():
    assert add("//;\n1;2") == 3

# Negative numbers raise an exception
def test_negative_numbers_raise_exception():
    try:
        add("1,-2,3")
    except ValueError as e:
        assert str(e) == "negative numbers not allowed -2"

def test_multiple_negatives_raise_exception():
    try:
        add("1,-1,2,-3")
    except ValueError as e:
        assert str(e) == "negative numbers not allowed -1,-3"
