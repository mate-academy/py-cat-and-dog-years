import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2])
    ],
    ids=[
        "both zero",
        "both under first year",
        "both at first year",
        "both at second year",
        "cat older than second year, "
        "dog at second year"
    ])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    ), f"Test failed for cat_age={cat_age}, dog_age={dog_age}"


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1),
        (-1, -1),
    ],
    ids=[
        "cat_age negative, dog_age valid",
        "cat_age valid, dog_age negative",
        "both negative"
    ])
def test_get_human_age_edge_cases(cat_age: int, dog_age: int) -> None:
    assert (
        get_human_age(cat_age, dog_age) == [0, 0]
    ), f"Test failed for cat_age={cat_age}, dog_age={dog_age}"


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("fifteen", 10),
        (10, "fifteen"),
        ("fifteen", "fifteen"),
        (None, 10),
        (10, None),
        (None, None),
    ],
    ids=[
        "cat_age string, dog_age valid",
        "cat_age valid, dog_age string",
        "both string",
        "cat_age None, dog_age valid",
        "cat_age valid, dog_age None",
        "both None"
    ])
def test_get_human_age_incorrect_type(
        cat_age: int | str | None,
        dog_age: int | str | None
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
