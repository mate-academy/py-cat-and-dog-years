import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result, test_id",
    [
        (-1, -2, [0, 0], "0 > cat/dog should convert into [0, 0]"),
        (0, 0, [0, 0], "0 cat/dog should convert into [0, 0]"),
        (14, 14, [0, 0], "14 cat/dog should convert into [0, 0]"),
        (15, 15, [1, 1], "15 cat/dog should convert into [1, 1]"),
        (23, 23, [1, 1], "23 cat/dog should convert into [1, 1]"),
        (24, 24, [2, 2], "24 cat/dog should convert into [2, 2]"),
        (27, 27, [2, 2], "27 cat/dog should convert into [2, 2]"),
        (28, 28, [3, 2], "28 cat/dog should convert into [3, 2]"),
        (95, 95, [19, 16], "95 cat/dog should convert into [19, 16]")
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list,
        test_id: str) -> None:
    assert get_human_age(cat_age, dog_age) == result


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
        exception: TypeError,
) -> None:
    with (pytest.raises(Exception)):
        get_human_age(cat_age, dog_age)
