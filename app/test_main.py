import pytest
from app.main import get_human_age


def test_get_human_age_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_below_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(1, 1) == [0, 0]
    assert get_human_age(10, 5) == [0, 0]
    assert get_human_age(7, 12) == [0, 0]


def test_get_human_age_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_between_thresholds() -> None:
    assert get_human_age(16, 16) == [1, 1]
    assert get_human_age(20, 20) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_after_second_threshold() -> None:
    assert get_human_age(25, 25) == [2, 2]
    assert get_human_age(26, 26) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_cat_dog_difference() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(29, 29) == [3, 3]


def test_get_human_age_cat_progression() -> None:
    assert get_human_age(28, 0) == [3, 0]
    assert get_human_age(32, 0) == [4, 0]
    assert get_human_age(36, 0) == [5, 0]
    assert get_human_age(40, 0) == [6, 0]


def test_get_human_age_dog_progression() -> None:
    assert get_human_age(0, 29) == [0, 3]
    assert get_human_age(0, 34) == [0, 4]
    assert get_human_age(0, 39) == [0, 5]
    assert get_human_age(0, 44) == [0, 6]


def test_get_human_age_large_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_get_human_age_asymmetric_ages() -> None:
    assert get_human_age(50, 30) == [8, 3]
    assert get_human_age(30, 50) == [3, 7]


def test_get_human_age_edge_cases() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 28) == [2, 2]
    assert get_human_age(28, 29) == [3, 3]


def test_get_human_age_remainder_discarded() -> None:
    assert get_human_age(26, 26) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(30, 26) == [3, 2]


def test_get_human_age_result_format() -> None:
    result = get_human_age(25, 30)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(age, int) for age in result)


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_get_human_age_examples(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
