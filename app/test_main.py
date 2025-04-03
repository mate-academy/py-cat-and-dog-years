from app.main import get_human_age


def test_get_human_age_when_both_ages_are_zero() -> None:
    result = get_human_age(0, 0)
    assert result == [0, 0]


def test_get_human_age_when_both_ages_are_14() -> None:
    result = get_human_age(14, 14)
    assert result == [0, 0]


def test_get_human_age_when_both_ages_are_15() -> None:
    result = get_human_age(15, 15)
    assert result == [1, 1]


def test_get_human_age_when_both_ages_are_24() -> None:
    result = get_human_age(24, 24)
    assert result == [2, 2]


def test_get_human_age_when_both_ages_are_100() -> None:
    result = get_human_age(100, 100)
    assert result == [21, 17]


def test_get_human_age_when_cat_is_14_and_dog_is_15() -> None:
    result = get_human_age(14, 15)
    assert result == [0, 1]


def test_get_human_age_when_cat_is_15_1_and_dog_is_15_1() -> None:
    result = get_human_age(15.1, 15.1)
    assert result == [1, 1]


def test_get_human_age_when_cat_is_23_and_dog_is_24() -> None:
    result = get_human_age(23, 24)
    assert result == [1, 2]


def test_get_human_age_when_cat_is_9_1_and_dog_is_9_1() -> None:

    result = get_human_age(9.1, 9.1)
    assert result == [0, 0]


def test_get_human_age_when_cat_is_15_and_dog_is_9() -> None:
    result = get_human_age(15, 9)
    assert result == [1, 0]


def test_get_human_age_when_cat_is_9_and_dog_is_15() -> None:
    result = get_human_age(9, 15)
    assert result == [0, 1]
