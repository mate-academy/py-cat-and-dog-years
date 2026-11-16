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
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_examples(cat_age: int, dog_age: int,
                                expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_sum_of_age_conversions() -> None:
    assert get_human_age(24, 29) == [2, 3]


def test_cat_age_conversion() -> None:
    assert get_human_age(28, 0) == [3, 0]


def test_dog_age_conversion() -> None:
    assert get_human_age(0, 29) == [0, 3]


def test_dog_output_changes_between_28_and_29() -> None:
    assert get_human_age(0, 28) == [0, 2]
    assert get_human_age(0, 29) == [0, 3]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-1, -1),
    ],
)
def test_negative_age_raises_value_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, None),
    ],
)
def test_invalid_age_type_raises_type_error(cat_age: int,
                                            dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
