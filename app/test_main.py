from app.main import get_human_age


def test_get_human_age_1_1() -> None:
    assert get_human_age(1, 1) == [0, 0], "1 cat year and 1 dog "
    "year should convert into 0 and 0 human age."


def test_get_human_age_14_14() -> None:
    assert get_human_age(14, 14) == [0, 0] , "14 cat years and 14 dog "
    "years should convert into 0 and 0 human age."


def test_get_human_age_15_15() -> None:
    assert get_human_age(15, 15) == [1, 1] , "15 cat years and 15 dog "
    "years should convert into 1 and 1 human age."


def test_get_human_age_23_23() -> None:
    assert get_human_age(23, 23) == [1, 1] , "23 cat years and 23 dog "
    "years should convert into 1 and 1 human age."


def test_get_human_age_24_24() -> None:
    assert get_human_age(24, 24) == [2, 2] , "24 cat years and 24 dog "
    "years should convert into 2 and 2 human age."


def test_get_human_age_27_27() -> None:
    assert get_human_age(27, 27) == [2, 2] , "27 cat years and 27 dog "
    "years should convert into 2 and 2 human age."


def test_get_human_age_28_28() -> None:
    assert get_human_age(28, 28) == [3, 2] , "28 cat years and 28 dog "
    "years should convert into 3 and 2 human age."


def test_get_human_age_100_100() -> None:
    assert get_human_age(100, 100) == [21, 17] , "100 cat years and 100 dog "
    "years should convert into 21 and 17 human age."


def test_get_human_age_15_24() -> None:
    assert get_human_age(15, 24) == [1, 2] , "15 cat years and 24 dog "
    "years should convert into 1 and 2 human age."


def test_get_human_age_28_15() -> None:
    assert get_human_age(28, 15) == [3, 1] , "28 cat years and 15 dog "
    "years should convert into 3 and 1 human age."


def test_get_human_age_100_28() -> None:
    assert get_human_age(100, 28) == [21, 2] , "100 cat years and 28 dog "
    "years should convert into 21 and 2 human age."
