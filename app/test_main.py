from app.main import get_human_age


def test_get_human_age_for_newborns() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_before_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_at_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_between_first_and_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_at_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_just_before_next_cat_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_just_after_cat_threshold() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_for_older_cat_and_dog() -> None:
    assert get_human_age(100, 100) == [21, 17]
