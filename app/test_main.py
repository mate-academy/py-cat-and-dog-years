from app.main import get_human_age


def test_ages_less_than_first_threshold() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_ages_exactly_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_ages_between_first_and_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_ages_exactly_second_threshold() -> None:
    # Рівно 24 роки = 2 людських (15 + 9)
    assert get_human_age(24, 24) == [2, 2]


def test_ages_beyond_second_threshold() -> None:
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
