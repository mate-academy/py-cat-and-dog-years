from app.main import get_human_age


def test_get_human_age_0_years_should_convert_into_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_14_years_should_convert_into_zero() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_15_years_should_convert_into_1() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_23_years_should_convert_into_1() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_24_years_should_convert_into_2() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_27_years_should_convert_into_2() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_28_years_should_convert_into() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_100_years_should_convert_into() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_get_human_age_years_should_convert_into_3() -> None:
    assert get_human_age(28, 29) == [3, 3]
