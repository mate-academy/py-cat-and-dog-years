from app.main import get_human_age


def test_with_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_with_cat_less_15_and_dog_less_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_with_cat_15_and_dog_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_with_cat_more_15_and_dog_less_15() -> None:
    assert get_human_age(23, 7) == [1, 0]


def test_with_cat_less_15_and_dog_more_15() -> None:
    assert get_human_age(12, 20) == [0, 1]


def test_with_cat_more_24_and_dog_more_24() -> None:
    assert get_human_age(25, 26) == [2, 2]


def test_with_cat_28_and_dog_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_with_cat_50_and_dog_50() -> None:
    assert get_human_age(50, 50) == [8, 7]
