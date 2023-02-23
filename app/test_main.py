from app.main import get_human_age


def test_an_array() -> bool:
    assert type(get_human_age(10, 3)) == list


def test_main_get_human_age() -> list:
    assert get_human_age(28, 28) == [3, 2]
