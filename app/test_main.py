from app.main import get_human_age


def test_should_return_expected_value():
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(28, 14) == [3, 0]
    assert get_human_age(14, 28) == [0, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
