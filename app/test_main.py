import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_years, dog_years, expected_result", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17])
])
def test_human_age_conversion(
    cat_years: int, dog_years: int, expected_result: list
) -> None:
    assert get_human_age(cat_years, dog_years) == expected_result
