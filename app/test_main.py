import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-10, -100, [0, 0])
    ],
    ids=[
        "for 0 years cat and dog 0",
        "for 14 years cat and dog similar",
        "for 15 years cat and dog similar",
        "for 23 years cat and dog similar all +1 year",
        "for 24 years cat and dog similar all +1 year",
        "for 27 years cat and dog similar all +1 year",
        "for 28 years cat +1 and dog different all +1 year",
        "for 100 years cat +1 and dog different all +1 year",
        "years is negative numbers"
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
    ],
    ids=[
        "TypeError for cat list",
        "TypeError for dog list",
        "TypeError for dog string",
        "TypeError for dog string",
    ]
)
def test_raising_errors_correctly(cat_age: int, dog_age: int, expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
