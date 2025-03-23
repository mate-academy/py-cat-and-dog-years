import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_age",
    [
        (-1, -10, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "human age should be 0 when input is negative integer",
        "human age should be 0 when input is 0",
        "human age should be 0 when input is 14 or less",
        "human age should be 1 when input is from 15 to 23",
        "human age should be 1 when input is from 15 to 23",
        "human age should be 2 for cat and dog when input is 24",
        "human age should be 2 for cat and dog when input is 27",
        "human age should be 3 for cat and 2 for dog when input is 28",
        "human age should be 21 for cat and 17 for dog when input is 100"
    ]
)
def test_count_human_age_correctly(cat_age: int,
                                   dog_age: int,
                                   expected_age: list[int]) -> None:

    assert get_human_age(cat_age, dog_age) == expected_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        (1, "1", TypeError),
        (1, [1], TypeError),
        (1, {1}, TypeError),
        (1, {"one": 1}, TypeError),
    ],
    ids=[
        "should raise TypeError when input has `str` type",
        "should raise TypeError when input has `list` type",
        "should raise TypeError when input has `set` type",
        "should raise TypeError when input has `dict` type",
    ]
)
def test_return_error_correctly(cat_age: int,
                                dog_age: int,
                                expected_error: Exception) -> None:

    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
