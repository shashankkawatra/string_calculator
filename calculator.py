
# Empty string returns 0
# Single number returns its value
# Two numbers comma-delimited returns their sum
# Multiple numbers comma-delimited returns their sum

def add(numbers):
    if not numbers:
        return 0
    parts = numbers.split(",")
    return sum(map(int, parts))
