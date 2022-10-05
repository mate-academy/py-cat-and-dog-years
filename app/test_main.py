from app.main import get_human_age


def test_cat_dog_zero_year() -> None:
    assert get_human_age(0, 0) == [0, 0], "expect list [0, 0]"


def test_cat_dog_less_15() -> None:
    assert get_human_age(9, 9) == [0, 0], "expect list [0, 0]"


def test_cat_dog_15() -> None:
    assert get_human_age(15, 15) == [1, 1], "expect list [1, 1]"


def test_cat_dog_more_15_less_24() -> None:
    assert get_human_age(22, 22) == [1, 1], "expect list [1, 1]"


def test_cat_dog_24() -> None:
    assert get_human_age(24, 24) == [2, 2], "expect list [2, 2]"


def test_cat_dog_more_24_less_28() -> None:
    assert get_human_age(27, 27) == [2, 2], "expect list [2, 2]"


def test_cat_dog_28() -> None:
    assert get_human_age(28, 28) == [3, 2], "expect list [3, 2]"


def test_cat_28_dog_29() -> None:
    assert get_human_age(28, 29) == [3, 3], "expect list [3, 3]"


def test_cat_dog_29() -> None:
    assert get_human_age(29, 29) == [3, 3], "expect list [3, 3]"


def test_cat_older() -> None:
    assert get_human_age(32, 16) == [4, 1], "expect list [4, 1]"


def test_dog_older() -> None:
    assert get_human_age(17, 41) == [1, 5], "expect list [1, 5]"
