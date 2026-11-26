import pytest
from app.main import get_human_age


def test_cat_should_get_extra_year_every_4_years() -> None:
    assert get_human_age(27, 0) == [2, 0]
    assert get_human_age(28, 0) == [3, 0]


def test_dog_should_get_extra_year_every_5_years() -> None:
    assert get_human_age(0, 28) == [0, 2]
    assert get_human_age(0, 29) == [0, 3]


def test_should_add_years_for_older_pets() -> None:
    assert get_human_age(32, 34) == [4, 4]


def test_should_raise_error_when_age_is_not_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("abc", 5)


def test_should_raise_error_when_dog_age_is_not_int() -> None:
    with pytest.raises(TypeError):
        get_human_age(5, "abc")


def test_should_return_zero_when_age_is_negative() -> None:
    assert get_human_age(-1, -4) == [0, 0]


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
        (100, 100, [21, 17])
    ]
)
def test_should_convert_age_correctly(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
