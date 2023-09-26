from app.main import get_human_age


def test_get_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_cat_only() -> None:
    assert get_human_age(14, 0) == [0, 0]
    assert get_human_age(15, 0) == [1, 0]
    assert get_human_age(23, 0) == [1, 0]
    assert get_human_age(24, 0) == [2, 0]
    assert get_human_age(27, 0) == [2, 0]
    assert get_human_age(28, 0) == [3, 0]
    assert get_human_age(100, 0) == [21, 0]


def test_get_human_age_dog_only() -> None:
    assert get_human_age(0, 14) == [0, 0]
    assert get_human_age(0, 15) == [0, 1]
    assert get_human_age(0, 23) == [0, 1]
    assert get_human_age(0, 24) == [0, 2]
    assert get_human_age(0, 27) == [0, 2]
    assert get_human_age(0, 28) == [0, 2]
    assert get_human_age(0, 100) == [0, 17]


def test_get_human_age_both() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
