import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (
            -6,
            6,
            ValueError,
        ),
        (
            "20",
            None,
            TypeError
        )
    ]
)
def test_errors(
        cat_age: int,
        dog_age: int,
        expected: type[ValueError | TypeError]
) -> None:
    with pytest.raises(expected):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (
            0,
            0,
            [0, 0]
        ),
        (
            14,
            14,
            [0, 0]
        ),
        (
            15,
            15,
            [1, 1]
        ),
        (
            23,
            23,
            [1, 1]
        ),
        (
            24,
            24,
            [2, 2]
        ),
        (
            28,
            29,
            [3, 3]
        ),
        (
            100,
            100,
            [21, 17]
        ),
    ]
)
def test_bound_values(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
