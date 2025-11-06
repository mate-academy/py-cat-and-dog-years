from app.main import get_human_age


def test_zero_age_should_return_zero() -> None:
    assert (
        get_human_age(0, 0) == [0, 0]
    ), "Dla (0, 0) oczekiwano [0, 0]"


def test_age_just_below_first_threshold_should_return_zero() -> None:
    assert (
        get_human_age(14, 14) == [0, 0]
    ), "Dla (14, 14) oczekiwano [0, 0]"


def test_age_at_first_threshold_should_return_one() -> None:
    assert (
        get_human_age(15, 15) == [1, 1]
    ), "Dla (15, 15) oczekiwano [1, 1]"


def test_age_just_below_second_threshold_should_return_one() -> None:
    assert (
        get_human_age(23, 23) == [1, 1]
    ), "Dla (23, 23) oczekiwano [1, 1]"

    assert (
        get_human_age(23, 16) == [1, 1]
    ), "Dla (23, 16) oczekiwano [1, 1]"


def test_age_at_second_threshold_should_return_two() -> None:
    assert (
        get_human_age(24, 24) == [2, 2]
    ), "Dla (24, 24) oczekiwano [2, 2]"


def test_cat_and_dog_age_just_below_next_human_year() -> None:
    assert (
        get_human_age(27, 28) == [2, 2]
    ), "Dla (27, 28) oczekiwano [2, 2] (reszta odrzucona)"


def test_conversion_to_three_human_years() -> None:
    assert (
        get_human_age(28, 28) == [3, 2]
    ), "Dla (28, 28) oczekiwano [3, 2] (pies ma tylko 2 lata ludzkie)"

    assert (
        get_human_age(29, 29) == [3, 3]
    ), "Dla (29, 29) oczekiwano [3, 3]"


def test_large_age_conversion() -> None:
    assert (
        get_human_age(100, 100) == [21, 17]
    ), "Dla (100, 100) oczekiwano [21, 17]"
