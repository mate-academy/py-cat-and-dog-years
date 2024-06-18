import pytest
from app.main import get_human_age


# write your code here
@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
    ]
)
def test_human_age(cat_age: int,
                   dog_age: int,
                   expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (1000, 1000, [246, 197]),
        (10000, 10000, [2496, 1997]),
    ]
)
def test_get_human_age_large_numbers(cat_age: int,
                                     dog_age: int,
                                     expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        (10, "10", TypeError),
    ],
    ids=[
        "Not integer value should raise TypeError",
    ]
)
def test_get_human_age_invalid_input(cat_age: int,
                                     dog_age: int,
                                     error: Exception) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
