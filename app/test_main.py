import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (1, 1, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (16, 16, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (29, 29, [3, 3]),
    (32, 32, [4, 3]),
    (33, 33, [4, 3]),
    (34, 34, [4, 4]),
    (100, 100, [21, 17]),
])
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list,
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_returns_list() -> None:
    result = get_human_age(15, 15)
    assert isinstance(result, list)
    assert len(result) == 2


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_just_below_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_exactly_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_diverge_at_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_dog_catches_up_at_29() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
