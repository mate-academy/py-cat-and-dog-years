import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-10, -100, [0, 0]),
        (1_000_000, 1_000_000, [249996, 199997])
    ],
    ids=[
        "for 0 years cat and dog 0 cat and dog are 0 years old",
        "cat and dog are 15 years old",
        "cat and dog are 23 years old",
        "cat and dog are 24 years old",
        "cat and dog are 27 years old",
        "cat and dog are 28 years old",
        "cat and dog are 100 years old",
        "cat and dog are negative numbers",
        "cat and dog are really large numbers"
    ]
)
def test_first(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        (0, [], TypeError),
        ([], 0, TypeError),
        (0, "", TypeError),
        ("", 0, TypeError),
        (0, {}, TypeError),
        ({}, 0, TypeError),
    ],
    ids=[
        "TypeError for cat list",
        "TypeError for dog list",
        "TypeError for cat string",
        "TypeError for dog string",
        "TypeError for cat dict",
        "TypeError for dog dict",
    ]
)
def test_raising_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
