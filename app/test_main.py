import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
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
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_returns_list() -> None:
    result = get_human_age(10, 10)
    assert isinstance(result, list)
    assert len(result) == 2


def test_get_human_age_takes_only_positive_numbers() -> None:
    with pytest.raises(TypeError):
        get_human_age(-5, -3)


def test_get_human_age_should_take_integers() -> None:
    with pytest.raises(TypeError):
        get_human_age("five", "twenty")
    with pytest.raises(TypeError):
        get_human_age(16.7, 20.1)
