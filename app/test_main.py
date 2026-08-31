from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (33, 33, [4, 3]),
        (34, 34, [4, 4]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0]),
        (-1, 15, [0, 1]),
        (26, -2, [2, 0]),
        (73, 17, [14, 1])
    ]
)
def test_should_return(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.6, 15),
        (15, 14.8),
        (15, None),
        (None, 19),
        (True, 19),
        (24, False)
    ]
)
def test_should_be_int_value(
        cat_age: int | float | str | None | bool,
        dog_age: int | float | str | None | bool
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
