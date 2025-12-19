from app.main import get_human_age


def test_cat0_dog0_under() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_cat0_dog0_upper() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_cat1_dog1_under() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_cat1_dog1_upper() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_cat2_dog2_under() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat2_dog2_upper() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat3_dog2_upper() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_cat21_dog17() -> None:
    assert get_human_age(100, 100) == [21, 17]
