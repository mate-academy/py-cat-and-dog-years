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
        (32, 32, [4, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_examples(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_zero_age_returns_zero_for_both() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_cat_first_bracket_upper_boundary() -> None:
    # 15 cat years -> exactly 1 human year (start of the 2nd bracket)
    assert get_human_age(15, 0)[0] == 1


def test_cat_first_bracket_just_below_boundary() -> None:
    # 14 cat years -> still 0 human years
    assert get_human_age(14, 0)[0] == 0


def test_cat_second_bracket_upper_boundary() -> None:
    # 15 + 9 = 24 cat years -> 2 human years (start of 4-year brackets)
    assert get_human_age(24, 0)[0] == 2


def test_cat_second_bracket_just_below_boundary() -> None:
    # 23 cat years -> still 1 human year
    assert get_human_age(23, 0)[0] == 1


def test_cat_third_bracket_progression() -> None:
    # Every 4 years after 24 gives 1 more human year
    assert get_human_age(27, 0)[0] == 2
    assert get_human_age(28, 0)[0] == 3
    assert get_human_age(31, 0)[0] == 3
    assert get_human_age(32, 0)[0] == 4


def test_dog_first_bracket_upper_boundary() -> None:
    # 15 dog years -> exactly 1 human year
    assert get_human_age(0, 15)[1] == 1


def test_dog_first_bracket_just_below_boundary() -> None:
    assert get_human_age(0, 14)[1] == 0


def test_dog_second_bracket_upper_boundary() -> None:
    # 15 + 9 = 24 dog years -> 2 human years (start of 5-year brackets)
    assert get_human_age(0, 24)[1] == 2


def test_dog_second_bracket_just_below_boundary() -> None:
    assert get_human_age(0, 23)[1] == 1


def test_dog_third_bracket_progression() -> None:
    # Every 5 years after 24 gives 1 more human year
    assert get_human_age(0, 28)[1] == 2
    assert get_human_age(0, 29)[1] == 3
    assert get_human_age(0, 33)[1] == 3
    assert get_human_age(0, 34)[1] == 4


def test_remainder_is_discarded_for_cat() -> None:
    # 26 cat years: 15 + 9 = 24 (2 years) + 2 leftover of the 4-year bracket
    # leftover doesn't count, so still 2 human years
    assert get_human_age(26, 0)[0] == 2


def test_remainder_is_discarded_for_dog() -> None:
    # 28 dog years: 15 + 9 = 24 (2 years) + 4 leftover of the 5-year bracket
    # leftover doesn't count, so still 2 human years
    assert get_human_age(0, 28)[1] == 2


def test_returns_list_of_two_elements() -> None:
    result = get_human_age(10, 10)
    assert isinstance(result, list)
    assert len(result) == 2


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
