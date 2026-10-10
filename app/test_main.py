import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (31, 33, [3, 3]),
        (32, 34, [4, 4]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, [0, 0]),
        (-15, -15, [0, 0]),
        (-100, -100, [0, 0]),
        (-1, 15, [0, 1]),
        (15, -1, [1, 0]),
    ],
)
def test_negative_ages(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 10),
        (10.5, 10),
        (None, 10),
        ([10], 10),
        (True, 10),
        (10, "10"),
        (10, 10.5),
        (10, None),
        (10, [10]),
        (10, True),
    ],
)
def test_invalid_age_type(cat_age: object, dog_age: object) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)


def test_returns_list_of_two_integers() -> None:
    result = main.get_human_age(50, 50)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(age, int) for age in result)
