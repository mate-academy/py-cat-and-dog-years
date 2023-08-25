import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected, test_id", [
    (0, 0, [0, 0], "zero_age"),
    (14, 14, [0, 0], "under_15_age"),
    (15, 15, [1, 1], "15_years"),
    (23, 23, [1, 1], "under_24_years"),
    (24, 24, [2, 2], "24_years"),
    (27, 27, [2, 2], "27_years"),
    (28, 28, [3, 2], "mixed_years"),
    (100, 100, [21, 17], "high_age"),
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: int,
        test_id: str
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
