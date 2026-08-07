import pytest

from app.main import get_human_age


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
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_examples(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_boundary_steps() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]

    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]

    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]

    assert get_human_age(28, 27) == [3, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(28, 29) == [3, 3]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-1, -1),
    ],
)
def test_get_human_age_rejects_negative_ages(
    cat_age: int,
    dog_age: int,
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (True, 15),
        (15, True),
    ],
)
def test_get_human_age_rejects_invalid_types(
    cat_age: int | str | float | bool,
    dog_age: int | str | float | bool,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
