import pytest

from app.main import get_human_age


def test_when_cat_and_dog_less_than_1_human_year() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_when_cat_and_dog_have_1_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_cat_and_dog_are_more_than_2_years_old() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (2, 3, [24, 15]),
    (0, 0, [0, 0]),
    (1, 0, [15, 0]),
    ("2", 3, ValueError),
    (2, "3", ValueError),
    (1.5, 3, ValueError),
    (2, 3.5, ValueError),
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list or type) -> None:
    if isinstance(expected, list):
        assert get_human_age(cat_age, dog_age) == expected
    else:
        with pytest.raises(expected):
            get_human_age(cat_age, dog_age)
