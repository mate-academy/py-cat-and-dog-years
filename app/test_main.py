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
        (29, 29, [3, 3]),
        (32, 33, [4, 3]),
        (36, 39, [5, 5]),
        (100, 100, [21, 17]),
        (28, 24, [3, 2]),
        (24, 29, [2, 3]),
    ],
)
def test_get_human_age_returns_correct_result(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
        (31, 3),
        (32, 4),
        (100, 21),
    ],
)
def test_cat_age_conversion(
    cat_age: int,
    expected: int,
) -> None:
    result: list[int] = get_human_age(cat_age, 0)

    assert result[0] == expected


@pytest.mark.parametrize(
    "dog_age, expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (28, 2),
        (29, 3),
        (33, 3),
        (34, 4),
        (100, 17),
    ],
)
def test_dog_age_conversion(
    dog_age: int,
    expected: int,
) -> None:
    result: list[int] = get_human_age(0, dog_age)

    assert result[1] == expected


def test_get_human_age_returns_two_elements() -> None:
    result: list[int] = get_human_age(28, 29)

    assert len(result) == 2
