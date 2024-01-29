from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected, test_id",
    [
        (0, 0, [0, 0], "0 cat/dog should convert into [0, 0]"),
        (-1, -1, [0, 0], "-1 cat/dog should convert into [0, 0]"),
        (14, 14, [0, 0], "14 cat/dog should convert into [0, 0]"),
        (15, 15, [1, 1], "15 cat/dog should convert into [1, 1]"),
        (23, 23, [1, 1], "23 cat/dog should convert into [1, 1]"),
        (24, 24, [2, 2], "24 cat/dog should convert into [2, 2]"),
        (28, 28, [2, 3], "28 cat/dog should convert into [2, 3]"),
        (27, 28, [2, 2], "cat-27/dog-28 should convert into [2, 2]"),
        (28, 29, [3, 3], "cat-28/dog-29 should convert into [3, 3]"),
        (100, 100, [21, 17], "100 cat/dog should convert into [21, 17]")
    ]
)
def test_checking_limit_values(
        cat_age: int,
        dog_age: int,
        expected: list,
        test_id: str
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected, test_id


@pytest.mark.parametrize(
    "cat_age,dog_age,exception",
    [
        pytest.param(
            10, "10", TypeError,
            id="should raise TypeError if dog age is not int"
        ),
        pytest.param(
            "10", 10, TypeError,
            id="should raise TypeError if cat age is not int")
    ]
)
def test_should_raises_the_correct_exception(
        cat_age: int,
        dog_age: int,
        exception: TypeError
) -> None:
    with (pytest.raises(exception)):
        get_human_age(cat_age, dog_age)
