import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "dog_age,cat_age,expected",
    [
        (-3, -11, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (1021300, 234123, [58526, 204257]),
    ]
)
def test_get_human_age(dog_age: int, cat_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_invalid_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat age is 10", "dog age is 11")
