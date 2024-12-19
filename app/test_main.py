from app.main import get_human_age, convert_to_human


def test_convert_to_human_age() -> None:
    assert convert_to_human(10, 15, 9, 4) == 0
    assert convert_to_human(20, 15, 9, 4) == 1
    assert convert_to_human(30, 15, 9, 4) == 3
    assert convert_to_human(40, 15, 9, 4) == 6
    assert convert_to_human(50, 15, 9, 4) == 8


def test_get_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(50, 50) == [8, 7]
    assert get_human_age(10, 20) == [0, 1]
    assert get_human_age(40, 25) == [6, 2]
