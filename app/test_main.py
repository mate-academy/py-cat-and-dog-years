from app.main import get_human_age


def test_should_return_0_for_first_14_animal_years() -> None:
    assert (
        get_human_age(14, 14) == [0, 0]
    ), "Should return 0 for first 14 animal years"


def test_should_return_1_for_first_15_23_animal_years() -> None:
    assert (
        get_human_age(15, 15) == get_human_age(23, 23)
    ), "Should return 1 for first 14-23 animal years"


def test_should_return_2_for_first_24_27_cat_and_24_28_dog_years() -> None:
    assert (
        get_human_age(24, 24) == get_human_age(27, 28)
    ), "Should return 1 for first 14-23 animal years"
