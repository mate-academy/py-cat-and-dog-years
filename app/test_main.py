import pytest

from app import main


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
        (100, 100, [21, 17]),
    ],
    ids=[
        "0 cat/dog years should convert into [0, 0] human years",
        "14 cat/dog years should convert into [0, 0] human years",
        "15 cat/dog years should convert into [1, 1] human years",
        "23 cat/dog years should convert into [1, 1] human years",
        "24 cat/dog years should convert into [2, 2] human years",
        "27 cat/dog years should convert into [2, 2] human years",
        "28 cat/dog years should convert into [3, 2] human years "
        "(cats and dogs use different intervals)",
        "100 cat/dog years should convert into [21, 17] human years",
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("10", 10),
        (10, "10"),
        (10.5, 10),
        (10, 10.5),
        (None, 10),
        (10, None),
        ([10], 10),
        (10, [10]),
        (True, 10),
        (10, False),
    ],
    ids=[
        "cat_age as str should raise TypeError",
        "dog_age as str should raise TypeError",
        "cat_age as float should raise TypeError",
        "dog_age as float should raise TypeError",
        "cat_age as None should raise TypeError",
        "dog_age as None should raise TypeError",
        "cat_age as list should raise TypeError",
        "dog_age as list should raise TypeError",
        "cat_age as bool should raise TypeError",
        "dog_age as bool should raise TypeError",
    ],
)
def test_get_human_age_raises_type_error(
    cat_age: object,
    dog_age: object
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
