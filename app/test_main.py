import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0, 0], id="age_equal_zero"),
        pytest.param(14, 14, [0, 0], id="14_years_edge_is_equal_zero"),
        pytest.param(15, 15, [1, 1], id="first_15_years_is_equal_one"),
        pytest.param(23, 23, [1, 1], id="23_years_edge_is_equal_one"),
        pytest.param(24, 24, [2, 2], id="next_9_years_is_equal_two"),
        pytest.param(27, 27, [2, 2], id="27_years_edge_is_equal_two"),
        pytest.param(28, 28, [3, 2], id="cat_next_4_years_is_equal_three"),
        pytest.param(28, 29, [3, 3], id="dog_next_5_years_is_equal_three"),
        pytest.param(100, 100, [21, 17], id="large_values_conversion")
    ]
)
def test_get_human_age_conversion(

        cat_age: int,
        dog_age: int,
        expected: list

) -> None:

    assert get_human_age(cat_age, dog_age) == expected
