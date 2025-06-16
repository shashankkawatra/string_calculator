
# Empty string returns 0
# Single number returns its value
# Two numbers comma-delimited returns their sum
# Multiple numbers comma-delimited returns their sum
# Newline as delimiter
# Custom delimiter support
# Negative numbers raise an exception

def add(numbers):
    if not numbers:
        return 0
    custom_delimiter = None
    if numbers.startswith("//"):
        delimiter_end = numbers.index("\n")
        custom_delimiter = numbers[2:delimiter_end]
        numbers = numbers[delimiter_end + 1:]
    if custom_delimiter:
        numbers = numbers.replace(custom_delimiter, ",")
    numbers = numbers.replace("\n", ",")
    parts = numbers.split(",")
    nums = list(map(int, parts))
    negatives = [str(n) for n in nums if n < 0]
    if negatives:
        return ValueError(f"negative numbers not allowed {','.join(negatives)}")
    return sum(nums)
