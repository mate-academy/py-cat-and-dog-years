import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "should execute for zeros",
        "14 should return [0, 0]",
        "15 should return [1, 1]",
        "23 should return [1, 1]",
        "24 should return [2, 2]",
        "28 should return [3, 2]",
        "100 should return [21, 17]",
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_exception",
    [
        ("string", "string", TypeError),
        (None, None, TypeError),
        (100, "string", TypeError),
        (100, [], TypeError),
        ([], 100, TypeError),
    ]
)
def test_get_human_age_invalid_data(cat_age: int,
                                    dog_age: int,
                                    expected_exception: Exception) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
