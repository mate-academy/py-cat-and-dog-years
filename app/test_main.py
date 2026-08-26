import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (99, 99, [20, 17]),
        (100, 100, [21, 17]),
    ]
)
def test_calculates_age_correctly(
    cat_age: int,
    dog_age: int,
    human_age: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        (-1, 0, ValueError),
        (0, -1, ValueError),
        (None, 0, TypeError),
        (0, None, TypeError),
        ("15", 0, TypeError),
        (0, "15", TypeError),
    ]
)
def test_raises_errors_correctly(
    cat_age: int | str | None,
    dog_age: int | str | None,
    error: type[Exception],
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
