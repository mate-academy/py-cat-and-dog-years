import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (-2, -3, [0, 0]),
        (-2, 3, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "0 cat and dog age must equal 0 in human age",
        "negative dog and cat age must equal 0 in human age",
        "negative cat age and 14 dog years must equal 0 in human age",
        "14 cat and dog years must equal 0 in human age",
        "15 cat and dog years must equal 1 in human age",
        "23 cat and dog years must equal 1 in human age",
        "24 cat and dog years must equal 2 in human age",
        "100 cat and dog years must equal 21 and 17 in human age"
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("two", -1),
        ("ten", "five"),
        (None, None),
    ],
    ids=[
        "TypeError raised when input is a string",
        "TypeError raised when input is a string",
        "TypeError raised when input is None"
    ],
)
def test_get_human_age_invalid_input(
        cat_age: int | str | None,
        dog_age: int | str | None
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
