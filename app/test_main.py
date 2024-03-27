from app.main import get_human_age


def test_should_return_zeros_when_age_less_15() -> None:
    assert (get_human_age(14, 14) == [0, 0]
            ), "should return zeros when age < 15"


def test_should_add_year_next_9_years() -> None:
    assert (get_human_age(24, 24) == [2, 2]
            ), "should add one year next 9 years after 15"


def test_should_add_next_years_after_24() -> None:
    assert (get_human_age(28, 28) == [3, 2]
            ), "should add one year for cat every 4 years, for dog 5 years"


def test_check_old_cat_and_dog() -> None:
    assert (get_human_age(100, 100) == [21, 17]
            ), "should be good with big datas"
