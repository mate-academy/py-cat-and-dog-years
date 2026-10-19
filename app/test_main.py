import pytest

from app import main


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected"),
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, -100, [0, 0]),
    ],
    ids=[
        "zero",
        "just-below-first-threshold",
        "first-threshold",
        "just-below-second-threshold",
        "second-threshold",
        "just-below-extra-year-thresholds",
        "extra-year-thresholds",
        "large-ages",
        "negative-ages",
    ],
)
def test_get_human_age_boundaries(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    ("cat_age", "dog_age"),
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
        (15, None),
        (True, 15),
        (15, False),
    ],
    ids=[
        "cat-string",
        "dog-string",
        "cat-float",
        "dog-float",
        "cat-none",
        "dog-none",
        "cat-bool",
        "dog-bool",
    ],
)
def test_get_human_age_rejects_non_integer_arguments(
    cat_age: object, dog_age: object
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
