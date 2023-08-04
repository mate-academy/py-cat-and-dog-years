from _pytest.python_api import raises

from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]


def test_get_human_age_negative_numbers() -> None:
    assert get_human_age(-5, 10) == [0, 1]
    assert get_human_age(10, -5) == [1, 0]
    assert get_human_age(-5, -5) == [0, 0]


def test_get_human_age_invalid_data_types() -> None:
    with raises(TypeError):
        get_human_age("10", 15)
    with raises(TypeError):
        get_human_age(10, "15")
    with raises(TypeError):
        get_human_age("10", "15")
    with raises(TypeError):
        get_human_age(10.5, 15)
    with raises(TypeError):
        get_human_age(10, 15.5)
    with raises(TypeError):
        get_human_age(10.5, 15.5)
