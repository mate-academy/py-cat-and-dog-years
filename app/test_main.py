from app.main import get_human_age


def test_zero_human_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_almost_one_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_cat_and_dog_one_human_year_old() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_cat_and_dog_two_human_years_old() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cats_get_older_faster() -> None:
    assert get_human_age(28, 28) == [3, 2], \
        ("Takes 4 cat/years and 5 dog/years for 1 human/year "
         "after they getting 2 years old.")


def test_bigger_age_difference_when_getting_older() -> None:
    assert get_human_age(100, 100) == [21, 17]
