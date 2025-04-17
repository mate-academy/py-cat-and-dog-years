from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(16, 16) == [1, 1]
    assert get_human_age(30, 30) == [3, 3]
    assert get_human_age(31, 31) == [3, 3]
    assert get_human_age(32, 32) == [4, 3]
    assert get_human_age(39, 39) == [5, 5]
    assert get_human_age(40, 40) == [6, 5]
    assert get_human_age(45, 45) == [7, 6]
    assert get_human_age(46, 46) == [7, 6]
