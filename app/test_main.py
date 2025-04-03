from app.main import get_human_age


def test_14_cat_and_dog_years() -> None:
    assert (
        get_human_age(14, 14) == [0, 0]
    ), "For 14 cat and dog years result should be [0, 0]"


def test_24_cat_and_dog_years() -> None:
    assert (
        get_human_age(24, 24) == [2, 2]
    ), "For 24 cat and dog years result should be [2, 2]"


def test_23_cat_and_dog_years() -> None:
    assert (
        get_human_age(23, 23) == [1, 1]
    ), "For 23 cat and dog years result should be [1, 1]"


def test_15_cat_and_dog_years() -> None:
    assert (
        get_human_age(15, 15) == [1, 1]
    ), "For 15 cat and dog years result should be [1, 1]"


def test_27_cat_and_28_dog_years() -> None:
    assert (
        get_human_age(27, 28) == [2, 2]
    ), "For 27 cat and 28 dog years result should be [2, 2]"


def test_28_cat_and_29_dog_years() -> None:
    assert (
        get_human_age(28, 29) == [3, 3]
    ), "For 28 cat and 29 dog years result should be [3, 3]"
