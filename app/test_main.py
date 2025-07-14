from app.main import get_human_age


def test_get_human_age_should_be_equal_for_cat_and_dog() -> None:
    assert (
        get_human_age(cat_age=24, dog_age=24) == [2, 2]
    )


def test_get_human_age_should_be_zero_for_both() -> None:
    assert (
        get_human_age(cat_age=0, dog_age=0) == [0, 0]
    )


def test_get_human_age_should_be_zero_for_cat() -> None:
    assert (
        get_human_age(cat_age=0, dog_age=40) == [0, 5]
    )


def test_get_human_age_should_be_zero_for_dog() -> None:
    assert (
        get_human_age(cat_age=40, dog_age=0) == [6, 0]
    )


def test_get_human_age_should_be_different_with_same_number() -> None:
    assert (
        get_human_age(cat_age=70, dog_age=70) == [13, 11]
    )


def test_get_human_age_cat_dog_age_should_be_zero() -> None:
    assert (
        get_human_age(cat_age=14, dog_age=14) == [0, 0]
    )


def test_get_human_age_cat_dog_age_should_be_one() -> None:
    assert (
        get_human_age(cat_age=23, dog_age=23) == [1, 1]
    )
