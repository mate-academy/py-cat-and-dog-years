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
    ]
)
def test_examples(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (16, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
        (31, 3),
        (32, 4),
        (35, 4),
        (36, 5),
        (100, 21),
    ]
)
def test_cat_age_boundaries(
    cat_age: int,
    expected: int
) -> None:
    assert get_human_age(cat_age, 0)[0] == expected


@pytest.mark.parametrize(
    "dog_age, expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (16, 1),
        (23, 1),
        (24, 2),
        (28, 2),
        (29, 3),
        (33, 3),
        (34, 4),
        (38, 4),
        (39, 5),
        (100, 17),
    ]
)
def test_dog_age_boundaries(
    dog_age: int,
    expected: int
) -> None:
    assert get_human_age(0, dog_age)[1] == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (28, 24, [3, 2]),
        (24, 29, [2, 3]),
        (40, 40, [6, 5]),
        (50, 60, [8, 9]),
        (100, 15, [21, 1]),
        (15, 100, [1, 17]),
    ]
)
def test_independent_age_conversion(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_result_is_list() -> None:
    assert isinstance(get_human_age(28, 29), list)


def test_result_contains_two_elements() -> None:
    assert len(get_human_age(28, 29)) == 2


def test_result_contains_integers() -> None:
    result: list[int] = get_human_age(28, 29)
    assert all(isinstance(age, int) for age in result)
