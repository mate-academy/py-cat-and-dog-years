import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (31, 31, [3, 3]),
        (32, 32, [4, 3]),
        (33, 33, [4, 3]),
        (34, 34, [4, 4]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list,
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
        (28, 24, [3, 2]),
        (24, 28, [2, 2]),
        (100, 0, [21, 0]),
        (0, 100, [0, 17]),
    ],
)
def test_cat_and_dog_ages_are_independent(
    cat_age: int,
    dog_age: int,
    expected: list,
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 0),
        (0, -1),
        (-1, -1),
        (-100, 100),
        (100, -100),
    ],
)
def test_negative_age_raises_value_error(
    cat_age: int,
    dog_age: int,
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
        (15, None),
        ([15], 15),
        (15, (15,)),
        (True, 15),
        (15, False),
    ],
)
def test_incorrect_type_raises_type_error(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


def test_returns_list_of_two_integers() -> None:
    result = get_human_age(50, 50)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(age, int) for age in result)
