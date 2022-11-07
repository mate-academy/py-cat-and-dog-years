from app.main import get_human_age


def test_zero_values() -> None:
    assert get_human_age(0, 0) == [0, 0], "test zero values"


def test_convert_1() -> None:
    assert get_human_age(15, 15) == [1, 1], "test convert to [1, 1] human ages"


def test_convert_2() -> None:
    assert get_human_age(14, 14) == [0, 0], "test convert to [0, 0] human ages"


def test_convert_3() -> None:
    assert get_human_age(23, 23) == [1, 1], "test convert to [1, 1] human ages"


def test_convert_4() -> None:
    assert get_human_age(24, 24) == [2, 2], "test convert to [2, 2] human ages"


def test_convert_5() -> None:
    assert get_human_age(27, 27) == [2, 2], "test convert to [2, 2] human ages"


def test_convert_6() -> None:
    assert get_human_age(28, 27) == [3, 2], "test convert to [3, 2] human ages"
