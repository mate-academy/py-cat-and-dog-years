import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age", "dog_age", "expected",
    [
        pytest.param(0, 0, [0, 0], id = "test_bottom_boundary_zero_year"),
        pytest.param(14, 14, [0, 0], id = "test_top_boundary_zero_year"),
        pytest.param(15, 15, [1, 1], id = "test_bottom_boundary_first_year"),
        pytest.param(23, 23, [1, 1], id = "test_top_boundary_first_year"),
        pytest.param(24, 24, [2, 2], id = "test_bottom_boundary_second_year"),
        pytest.param(27, 27, [2, 2], id = "test_top_boundary_second_year"),
        pytest.param(28, 28, [3, 2], id = "test_cat_age_less_dog_year"),
        pytest.param(100, 100, [21, 17], id = "test_cat_age_more_dog_year")
    ]
)
def test_function(cat_age, dog_age, expected) -> None:
    assert get_human_age(cat_age, dog_age) == expected
