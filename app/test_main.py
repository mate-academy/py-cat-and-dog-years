import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_age",
    [
        (
            0,
            0,
            [0, 0],
        ),
        (
            27,
            28,
            [2, 2],
        ),
        (
            15,
            15,
            [1, 1],
        ),
        (
            28,
            29,
            [3, 3]
        ),
        (
            24,
            24,
            [2, 2]
        ),
    ]
)
def test_calculate_age_correctly(
    cat_age: int,
    dog_age: int,
    expected_age: list,
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age
