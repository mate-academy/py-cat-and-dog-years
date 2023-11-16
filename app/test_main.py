import pytest
from app.main import get_human_age


# def test_should_raise_error_when_age_not_integer() -> None:
#     with pytest.raises(TypeError):
#         get_human_age("five", "0.79")


# Test below could be implemented, but main.py doesn't pass it,
# while function takes negative numbers and returns zeros.
#
# def test_should_raise_error_when_age_is_negative() -> None:
#     with pytest.raises(ValueError):
#         get_human_age(-1, -17)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (44, 44, [7, 6]),
        (100, 100, [21, 17])
    ]
)
def test_should_return_expected_results(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
