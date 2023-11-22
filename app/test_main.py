from app.main import get_human_age


# write your code here
def test_should_return_0_human_years_for_first_14_cat_and_dog_years():
    for year in range(15):
        assert get_human_age(year, year) == [0, 0]


def test_should_return_1_human_years_from_15_to_23_cat_and_dog_years():
    for year in range(15, 24):
        assert get_human_age(year, year) == [1, 1]


def test_should_return_2_human_years_for_24_cat_and_dog_years():
    assert get_human_age(24, 24) == [2, 2]


def test_should_add_1_human_years_every_4_years_for_a_cat_over_23():
    assert get_human_age(27, 0)[0] == 2
    assert get_human_age(28, 0)[0] == 3
    assert get_human_age(100, 0)[0] == 21


def test_should_add_1_human_years_every_4_years_for_a_dog_over_23():
    assert get_human_age(0, 28)[1] == 2
    assert get_human_age(0, 29)[1] == 3
    assert get_human_age(0, 100)[1] == 17
