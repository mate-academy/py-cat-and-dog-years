from app.main import get_human_age


def test_zero_ages() -> None:
    human_age = get_human_age(0, 0)
    assert human_age == [0, 0]


def test_first_year() -> None:
    human_age = get_human_age(15, 15)
    assert human_age == [1, 1]


def test_second_year() -> None:
    human_age = get_human_age(24, 24)
    assert human_age == [2, 2]


def test_cat_dog_each_year() -> None:
    human_age = get_human_age(28, 29)
    assert human_age == [3, 3]


def test_different_results_cat_dog() -> None:
    human_age = get_human_age(100, 100)
    assert human_age == [21, 17]
