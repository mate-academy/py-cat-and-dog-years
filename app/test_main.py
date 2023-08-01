from app.main import get_human_age


def test_both_zero_age() -> None:
    cat_age, dog_age = 0, 0
    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_both_under_15_years() -> None:
    cat_age, dog_age = 14, 14
    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_both_15_years() -> None:
    cat_age, dog_age = 15, 15
    assert get_human_age(cat_age, dog_age) == [1, 1]


def test_both_just_over_15_years() -> None:
    cat_age, dog_age = 23, 23
    assert get_human_age(cat_age, dog_age) == [1, 1]


def test_both_exactly_1_more_year() -> None:
    cat_age, dog_age = 24, 24
    assert get_human_age(cat_age, dog_age) == [2, 2]


def test_both_just_over_1_more_year() -> None:
    cat_age, dog_age = 27, 27
    assert get_human_age(cat_age, dog_age) == [2, 2]


def test_cat_1_more_year_than_dog() -> None:
    cat_age, dog_age = 28, 24
    assert get_human_age(cat_age, dog_age) == [3, 2]


def test_both_just_over_2_more_years() -> None:
    cat_age, dog_age = 100, 100
    assert get_human_age(cat_age, dog_age) == [21, 17]
