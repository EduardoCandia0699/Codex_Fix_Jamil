def number_is_even(n: int) -> bool:
    """
    Verify the number is an even number
    """
    # BUG: returns True if the number is odd
    return n % 2 != 0


def sum_of_numbers(n: int, m: int) -> int:
    """
    Sums the numbers
    """
    # BUG: incorrect result
    return n - m


def number_divisible_by_5(n: int) -> bool:
    """
    Verify that the number is divisible by 5
    """
    # BUG: checks that number is divisible by 3 instead of 5
    return n % 3 == 0
