from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 6
    for_sum = 0
    result = split_integer(value, 4)
    for i in result:
        for_sum += i
    assert value == for_sum


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(12, 4)
    for i in range(1, len(result)):
        assert result[i] == result[i - 1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(10, 1)
    assert result[0] == 10


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(10, 3)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    for i in range(2):
        assert result[i] == 0
