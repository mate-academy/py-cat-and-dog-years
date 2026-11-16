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
def test_get_human_age_examples(cat_age: int, dog_age: int,
                                expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_age_before_first_boundary() -> None:
    assert get_human_age(14, 0) == [0, 0]


def test_cat_age_at_first_boundary() -> None:
    assert get_human_age(15, 0) == [1, 0]


def test_cat_age_before_second_boundary() -> None:
    assert get_human_age(23, 0) == [1, 0]


def test_cat_age_at_second_boundary() -> None:
    assert get_human_age(24, 0) == [2, 0]


def test_dog_age_before_first_boundary() -> None:
    assert get_human_age(0, 14) == [0, 0]


def test_dog_age_at_first_boundary() -> None:
    assert get_human_age(0, 15) == [0, 1]


def test_dog_age_before_second_boundary() -> None:
    assert get_human_age(0, 23) == [0, 1]


def test_dog_age_at_second_boundary() -> None:
    assert get_human_age(0, 24) == [0, 2]


def test_cat_and_dog_have_different_conversion_rates() -> None:
    assert get_human_age(28, 28) == [3, 2]
