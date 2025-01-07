from app.main import get_human_age, convert_to_human


def test_get_human_age():
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
    assert get_human_age(16, 0) == [1, 0]
    assert get_human_age(0, 16) == [0, 1]
    assert get_human_age(24, 15) == [2, 1]
    assert get_human_age(15, 24) == [1, 2]


def test_convert_to_human():
    assert convert_to_human(0, 15, 9, 4) == 0
    assert convert_to_human(15, 15, 9, 4) == 1
    assert convert_to_human(24, 15, 9, 4) == 2
    assert convert_to_human(28, 15, 9, 4) == 3
    assert convert_to_human(100, 15, 9, 4) == 21
