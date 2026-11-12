from __future__ import annotations

import pytest

from app.main import get_human_age


def test_zero_age_returns_zero_human_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_below_first_threshold_returns_zero_human_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_threshold_returns_one_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_between_first_and_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_second_threshold_returns_two_human_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_age_before_third_threshold_returns_two_human_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_and_dog_have_different_third_threshold() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_age_returns_expected_human_years() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_cat_age_is_converted_correctly() -> None:
    assert get_human_age(28, 0)[0] == 3


def test_dog_age_is_converted_correctly() -> None:
    assert get_human_age(0, 28)[1] == 2


def test_result_contains_two_elements() -> None:
    result = get_human_age(100, 100)

    assert len(result) == 2


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
def test_get_human_age_returns_expected_result(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
