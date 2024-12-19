from app.main import get_human_age


def test_first_cat_and_dog_years():
    assert (
        get_human_age(14, 14) == [0, 0]
    )


def test_first_cat_and_dog_years_with_a_critical_value():
    assert (
        get_human_age(15, 15) == [1, 1]
    )


def test_second_cat_and_dog_years():
    assert (
        get_human_age(23, 23) == [1, 1]
    )


def test_third_cat_and_dog_years():
    assert (
        get_human_age(27, 27) == [2, 2]
    )


def test_second_cat_and_dog_years_with_a_difference_age():
    assert (
        get_human_age(28, 28) == [3, 2]
    )


def test_third_years_with_a_critical_value():
    assert (
        get_human_age(100, 100) == [21, 17]
    )
