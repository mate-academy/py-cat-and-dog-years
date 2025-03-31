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
        (27, 27, [2, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "check if cat and dog age 0 equals 0",
        "cat and dog age 14 should be equal to 0",
        "cat and dog age 15 should be equal to 1",
        "cat and dog age 23 should be equal to 1",
        "cat and dog age 24 should be equal to 2",
        "cat and dog age 27 should be equal to 2",
        "cat and dog age 100 should be equal to 21 and 17"
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("one", "two"),
        (None, None)
    ],
    ids=[
        "TypeError raised when got string not int",
        "TypeError raised when got None not int"
    ]
)
def test_get_human_age_errors(
        cat_age: int | str | None,
        dog_age: int | str | None
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
