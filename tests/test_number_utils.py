from src.number_utils import number_is_even, sum_of_numbers, number_divisible_by_5


def test_number_is_even():
    assert number_is_even(10)


def test_number_is_odd():
    assert not number_is_even(9)


def test_sum_of_numbers():
    assert sum_of_numbers(9, 10) == 19


def test_number_divisible_by_5():
    assert number_divisible_by_5(50)


def test_number_not_divisible_by_5():
    assert not number_divisible_by_5(44)
