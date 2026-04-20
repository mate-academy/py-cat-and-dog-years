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
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero_ages",
        "less_than_15",
        "exactly_15",
        "between_15_and_23",
        "exactly_24",
        "before_next_step",
        "cat_faster_than_dog",
        "large_ages",
    ],
)
def test_examples(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_less_than_15() -> None:
    assert get_human_age(10, 13) == [0, 0]


def test_from_15_to_23() -> None:
    assert get_human_age(15, 20) == [1, 1]


def test_exactly_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_step_after_24() -> None:
    assert get_human_age(28, 24) == [3, 2]


def test_dog_step_after_24() -> None:
    assert get_human_age(24, 29) == [2, 3]
