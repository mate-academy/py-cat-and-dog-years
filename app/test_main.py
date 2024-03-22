import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (29, 28, [3, 2]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197]),
    ]
)
def test_can_count_years(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        (-1, 5, ValueError),
        (5, -1, ValueError),
        (5.5, 5, TypeError),
        ("5", 5, TypeError),
    ]
)
def test_can_count_years_error(
        cat_age: int,
        dog_age: int,
        expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
