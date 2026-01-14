import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(14, 14, [0, 0],
                     id="test_zero_values_returns_list_of_two_zeros"),
        pytest.param(15, 15, [1, 1],
                     id="test_values_to_get_one_human_year"),
        pytest.param(23, 23, [1, 1],
                     id="test_values_to_get_two_human_years"),
        pytest.param(24, 24, [2, 2],
                     id="test_values_to_get_two_human_years"),
        pytest.param(27, 27, [2, 2],
                     id="test_values_to_get_two_and_two_human_years"),
        pytest.param(28, 28, [3, 2],
                     id="test_values_to_get_three_and_two_human_years"),
        pytest.param(32, 34, [4, 4],
                     id="test_values_to_get_three_and_more_human_years"),
        pytest.param(100, 100, [21, 17],
                     id="test_values_to_get_larger_human_years"),
    ]
)
def test_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    ), (f"Cat age: {cat_age} and Dog age:{dog_age}"
        f" should be equal to {expected}")
