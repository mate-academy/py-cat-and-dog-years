from app.main import get_human_age


def test_get_human_age_should_return_0_when_age_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(1, 1) == [0, 0]


def test_get_human_age_should_return_2_when_age_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_human_age_for_ages_higher_than_24() -> None:
    assert get_human_age(55, 81) == [9, 13]
    assert get_human_age(27, 28) == [2, 2]
    assert get_human_age(28, 29) == [3, 3]


def test_human_age_should_return_1_when_age_15() -> None:
    assert get_human_age(15, 15) == [1, 1]
