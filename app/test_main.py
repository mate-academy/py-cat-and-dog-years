from app.main import get_human_age


def test_first_15_years_give_one_human_year() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 14) == [1, 0]
    assert get_human_age(14, 15) == [0, 1]
    assert get_human_age(14, 15) == [0, 1]
    assert get_human_age(15, 15) == [1, 1]


def test_next_nine_years_give_one_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 23) == [2, 1]
    assert get_human_age(23, 24) == [1, 2]
    assert get_human_age(24, 24) == [2, 2]


def test_next_four_years_give_one_cat_and_five_to_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(28, 29) == [3, 3]
    assert get_human_age(28, 29) == [3, 3]
    assert get_human_age(100, 100) == [21, 17]
