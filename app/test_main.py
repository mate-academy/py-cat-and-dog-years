from app.main import get_human_age, convert_to_human


def test_an_array() -> bool:
    assert type(get_human_age(10, 3)) == list


def test_main_get_human_age() -> list:
    assert get_human_age(28, 28) == [3, 2]


def test_main_get_human_age1() -> list:
    assert get_human_age(22, 20) == [1, 1]


def test_convert_to_human() -> int:
    assert convert_to_human(14, 14, 9, 4) == 1
