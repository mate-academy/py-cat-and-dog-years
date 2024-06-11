import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (1, 1, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_cat_or_dog_yars(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,typeerror",
    [
        ("25", 0, TypeError),
        (15, "0", TypeError),
        ({1: 2}, [], TypeError),
    ]
)
def test_cat_integer(cat_age, dog_age, typeerror) -> None:
    with pytest.raises(typeerror):
        get_human_age(cat_age, dog_age)


def test_length_return_get_human_age() -> None:
    assert len(get_human_age(0, 0)) == 2


