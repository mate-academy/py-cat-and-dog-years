from app.main import get_human_age


def test_zero_values() -> None:
    assert get_human_age(0, 0) == [0, 0], "test zero values"


def test_should_convert_into_zero_human_age() -> None:
    assert get_human_age(14, 14) == [0, 0], "test convert to [0, 0] human ages"


def test_should_convert_into_one_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1], "test convert to [1, 1] human ages"


def test_should_convert_into_one_human_age2() -> None:
    assert get_human_age(23, 23) == [1, 1], "test convert to [1, 1] human ages"


def test_should_convert_into_two_human_ages() -> None:
    assert get_human_age(24, 24) == [2, 2], "test convert to [2, 2] human ages"


def test_should_convert_into_two_human_ages2() -> None:
    assert get_human_age(27, 28) == [2, 2], "test convert to [2, 2] human ages"


def test_should_convert_into_three_human_agees() -> None:
    assert get_human_age(28, 29) == [3, 3], "test convert to [3, 3] human ages"
