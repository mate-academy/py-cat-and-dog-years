from app.main import get_human_age


def test_length_return_get_human_age() -> None:
    assert len(get_human_age(0, 0)) == 2


def test_cat_integer() -> None:
    assert isinstance(get_human_age(100, 100)[0], int)


def test_dog_integer() -> None:
    assert isinstance(get_human_age(100, 100)[1], int)


def test_if_cat_or_dog_14_yars() -> None:
    assert get_human_age(1, 1) == [0, 0]


def test_if_cat_or_dog_15_yars() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_if_cat_or_dog_24_yars() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_if_cat_or_dog_28_yars() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_if_cat_or_dog_100_yars() -> None:
    assert get_human_age(100, 100) == [21, 17]
