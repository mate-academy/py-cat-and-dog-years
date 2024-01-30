from app.main import get_human_age


def test_all_age_is_equal_zeros() -> None:
    assert (get_human_age(0, 0) == [0, 0]
            ), "Result should be equal [0, 0]"


def test_first_15_animal_years_equal_1_human_year() -> None:
    assert (get_human_age(15, 15) == [1, 1]
            ), "Result should be equal [1, 1]"


def test_less_than_15_animal_years_equal_0_human_year() -> None:
    assert (get_human_age(10, 10) == [0, 0]
            ), "Result should be equal [0, 0]"


def test_next_9_animal_years_equal_1_human_year() -> None:
    assert (get_human_age(27, 27) == [2, 2]
            ), "Result should be equal [2, 2]"


def test_every_4_after_24_cat_years_is_equal_plus1_human_year() -> None:
    assert (get_human_age(28, 28) == [3, 2]
            ), "Result should be equal [3, 2]"


def test_every_5_after_24_dog_years_is_equal_plus1_human_year() -> None:
    assert (get_human_age(29, 29) == [3, 3]
            ), "Result should be equal [3, 3]"


def test_verify_to_correct_age_converter_in_long_period():
    assert (get_human_age(100, 100) == [21, 17]
            ), "Result should be equal [21, 17]"
