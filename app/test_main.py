import pytest
from app.main import get_human_age


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
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_parametrized(cat_age: int,
                                    dog_age: int,
                                    expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_and_dog_age_independent() -> None:
    cat_only = get_human_age(28, 0)[0]
    dog_only = get_human_age(0, 28)[1]
    assert cat_only == 3
    assert dog_only == 2


def test_large_values() -> None:
    result = get_human_age(400, 400)
    assert result[0] > 50
    assert result[1] > 50
