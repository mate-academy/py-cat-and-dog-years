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
        (-1, -1, [0, 0])
    ],
    ids=[
        "(0, 0) cat/dog years should be converted to [0, 0]",
        "(14, 14) cat/dog years should be converted to [0, 0]",
        "(15, 15) cat/dog years should be converted to [1, 1]",
        "(23, 23) cat/dog years should be converted to [1, 1]",
        "(24, 24) cat/dog years should be converted to [2, 2]",
        "(27, 27) cat/dog years should be converted to [2, 2]",
        "(28, 28) cat/dog years should be converted to [3, 2]",
        "(100, 100) cat/dog years should be converted to [21, 17]",
        "Invalid input should return [0, 0]",
    ]
)
def test_convert_to_human_age_correctly(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("3", 3),
        (4, "5")
    ]
)
def test_raising_correct_exception(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
