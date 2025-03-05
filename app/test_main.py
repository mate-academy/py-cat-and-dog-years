from app.main import get_human_age


def test_0_human_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_0_human_age_but_14_cat_and_dog() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_1_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_1_human_age_but_23_cat_dog() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_2_human_age() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_2_human_age_but_27_cat_dog() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_3_human_age() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_such_a_big_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
