from app.main import get_human_age

def test_should_return_zero_for_zero_cat_and_dog_age() -> None:
    assert get_human_age(0, 0) == [0, 0], (
        "Expected [0, 0] for input (0, 0)."
    )


def test_should_return_zero_for_cat_and_dog_age_14() -> None:
    assert get_human_age(14, 14) == [0, 0], (
        "Expected [0, 0] for input (14, 14)."
    )


def test_should_return_one_for_cat_and_dog_age_15() -> None:
    assert get_human_age(15, 15) == [1, 1], (
        "Expected [1, 1] for input (15, 15)."
    )


def test_should_return_one_for_cat_and_dog_age_23() -> None:
    assert get_human_age(23, 23) == [1, 1], (
        "Expected [1, 1] for input (23, 23)."
    )


def test_should_return_two_for_cat_and_dog_age_24() -> None:
    assert get_human_age(24, 24) == [2, 2], (
        "Expected [2, 2] for input (24, 24)."
    )


def test_should_return_three_and_two_for_cat_and_dog_age_28() -> None:
    assert get_human_age(28, 28) == [3, 2], (
        "Expected [3, 2] for input (28, 28)."
    )


def test_should_return_twenty_one_and_seventeen_for_cat_and_dog_age_100() -> None:
    assert get_human_age(100, 100) == [21, 17], (
        "Expected [21, 17] for input (100, 100)."
    )
