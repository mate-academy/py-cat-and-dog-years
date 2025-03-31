import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_result, test_id", [
    (0, 0, [0, 0], "Zero age"),
    (-5, -5, [0, 0], "Negative age"),
    (14, 14, [0, 0], "14 cat/dog years should convert into 0 human age"),
    (23, 23, [1, 1], "23 cat/dog years should convert into 1 human age"),
    (24, 24, [2, 2], "24 cat/dog years should convert into 2 human age"),
    (29, 30, [3, 3], "Cat / dog crosses third range"),
    (33, 35, [4, 4], "Cat / dog crosses 4 range"),
    (10000, 10000, [2496, 1997], "Large numbers"),
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list,
        test_id: str) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
