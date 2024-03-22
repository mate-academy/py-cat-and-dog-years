import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_value",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 29, [3, 3]),
        (23, 23, [1, 1]),
        (27, 28, [2, 2]),
        (30, 31, [3, 3]),
        (100, 100, [21, 17]),
        (-24, -100, [0, 0])
    ],
    ids=[
        "0 should return 0",
        "should return 0 if values < 1 human age",
        "should return 1 human year",
        "should return 2 human year",
        "should return 3 human year",
        "should return 1 (discard the remainder)",
        "should return 2 (discard the remainder)",
        "should return 3 (discard the remainder)",
        "large values test",
        "negative values should return 0"
    ]
)
def test_expected_human_age_value(
        cat_age: int,
        dog_age: int,
        expected_value: list
) -> None:
    assert get_human_age(cat_age=cat_age, dog_age=dog_age) == expected_value


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        ("1", 0, TypeError),
        (None, 0, TypeError)
    ]
)
def test_raise_expected_error(
        cat_age: int,
        dog_age: int,
        expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
