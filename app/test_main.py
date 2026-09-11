import pytest

from app.main import get_human_age


def test_zero_age_gives_zero_human_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


@pytest.mark.parametrize("age", [1, 5, 10, 14])
def test_age_below_fifteen_gives_zero_human_age(age: int) -> None:
    assert get_human_age(age, age) == [0, 0]


def test_age_exatly_fifteen_given_one_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_just_before_second_human_year_still_gives_one_human_year(
) -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_twenty_four_given_two_years_human_for_bout() -> None:
    assert get_human_age(24, 24) == [2, 2]


@pytest.mark.parametrize("age", [25, 26, 27])
def test_cat_stays_at_two_human_years_until_twenty_seven(age: int) -> None:
    cat_age, _ = get_human_age(age, 0)
    assert cat_age == 2


def test_cat_reaches_three_human_years_at_twenty_eight() -> None:
    cat_age, _ = get_human_age(28, 0)
    assert cat_age == 3


@pytest.mark.parametrize("age", [25, 26, 27, 28])
def test_dog_stays_at_two_human_years_until_twenty_eight(age: int) -> None:
    _, dog_age = get_human_age(0, age)
    assert dog_age == 2


def test_dog_reaches_three_human_years_at_twenty_nine() -> None:
    _, dog_age = get_human_age(0, 29)
    assert dog_age == 3


def test_cat_four_years_blocks_increment_human_age_by_one() -> None:
    cat_age_28, _ = get_human_age(28, 0)
    cat_age_32, _ = get_human_age(32, 0)
    cat_age_36, _ = get_human_age(36, 0)
    assert cat_age_28 == 3
    assert cat_age_32 == 4
    assert cat_age_36 == 5


def test_dog_five_years_blocks_increment_human_age_by_one() -> None:
    _, dog_age_29 = get_human_age(0, 29)
    _, dog_age_34 = get_human_age(0, 34)
    _, dog_age_39 = get_human_age(0, 39)
    assert dog_age_29 == 3
    assert dog_age_34 == 4
    assert dog_age_39 == 5


def test_partial_block_does_not_add_extra_year() -> None:
    cat_age, _ = get_human_age(31, 0)
    _, dog_age = get_human_age(0, 33)
    assert cat_age == 3
    assert dog_age == 3


def test_large_ages_match_expected_totals() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_result_list_of_two_integers() -> None:
    result = get_human_age(10, 40)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(age, int) for age in result)
