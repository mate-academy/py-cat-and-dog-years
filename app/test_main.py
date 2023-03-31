import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        (-14, -14, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        ("14", 14, TypeError),
        (14, "14", TypeError),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected_human_age: int) -> None:
    if expected_human_age == TypeError:
        with pytest.raises(expected_human_age):
            get_human_age(cat_age, dog_age)
    else:
        assert get_human_age(cat_age, dog_age) == expected_human_age
