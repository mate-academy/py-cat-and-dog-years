import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (32, 32, [4, 3]),
        (33, 33, [4, 3]),
        (34, 34, [4, 4]),
        (100, 100, [21, 17])
    ]
)
def test_years_add_borders(
    cat: int,
    dog: int,
    result: list
) -> None:
    assert get_human_age(cat, dog) == result


@pytest.mark.parametrize(
    "cat, dog",
    [
        (-1, 0),
        (0, -1),
        (-1, -1)
    ]
)
def test_error_negative_years(
    cat: int,
    dog: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat, dog)


@pytest.mark.parametrize(
    "cat, dog",
    [
        ("cat", "dog"),
        (1.5, 15.6),
        (True, False),
        ([1, 1], [1, 1]),
        ((1, 1), (1, 1)),
        ({1, 1}, {1, 1}),
        ({"a": 1, "b": 2}, {"1": "a", "2": "b"})
    ]
)
def test_type_of_age_args(
    cat: Any,
    dog: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat, dog)
