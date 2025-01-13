from app.main import get_human_age

def test_get_human_ages_zero_ages() -> None:
    assert (
        get_human_age(0,0) == [0, 0]
    )

def test_get_human_age_cat_14_dog_14() -> None:
    assert (
            get_human_age(14, 14) == [0, 0]
    )

def test_get_human_age_cat_15_dog_15() -> None:
    assert (
            get_human_age(15, 15) == [1, 1]
    )

def test_get_human_age_cat_23_dog_23() -> None:
    assert (
            get_human_age(23, 23) == [1, 1]
    )

def test_get_human_age_cat_24_dog_24() -> None:
    assert (
            get_human_age(24, 24) == [2, 2]
    )


def test_get_human_age_cat_27_dog_27() -> None:
    assert (
            get_human_age(27, 27) == [2, 2]
    )

def test_get_human_age_cat_28_dog_28() -> None:
    assert (
            get_human_age(28, 28) == [3, 2]
    )


def test_get_human_age_cat_100_dog_100() -> None:
    assert (
            get_human_age(100, 100) == [21, 17]
    )
