from app import main
import pytest


@pytest.mark.parametrize(
    "cat, dog, expected_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_if_conversion_rate_is_correct(
    cat: int,
    dog: int,
    expected_age: list,
) -> None:
    assert main.get_human_age(cat, dog) == expected_age


@pytest.mark.parametrize(
    "first_wrong_input, second_wrong_input, expected_error",
    [
        (-3, -3, ValueError),
        (234987243, 234987243, ValueError),
    ],
)
def test_for_not_normal_range_input(
    first_wrong_input: int,
    second_wrong_input: int,
    expected_error: Exception,
) -> None:
    with pytest.raises(expected_error):
        main.get_human_age(first_wrong_input, second_wrong_input)


@pytest.mark.parametrize(
    "first_false_type, second_false_type, expected_exception",
    [
        ("fifteen", "fifteen", TypeError),
        (True, False, TypeError),
        (17.1, 19.47, TypeError),
    ],
)
def test_for_correct_exception(
    first_false_type: str | bool | float,
    second_false_type: str | bool | float,
    expected_exception: type[Exception],
) -> None:
    with pytest.raises(expected_exception):
        main.get_human_age(first_false_type, second_false_type)
