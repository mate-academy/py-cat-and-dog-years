from app.main import get_human_age


def test_should_check_when_cat_and_dog_year_is_equal_0():
    assert get_human_age(0, 0) == [0, 0]


def test_should_check_when_cat_and_dog_year_is_equal_14():
    assert get_human_age(14, 14) == [0, 0]


def test_should_check_when_cat_and_dog_year_is_equal_15():
    assert get_human_age(15, 15) == [1, 1]


def test_should_check_when_cat_and_dog_year_is_equal_23():
    assert get_human_age(23, 23) == [1, 1]


def test_should_check_when_cat_and_dog_year_is_equal_24():
    assert get_human_age(24, 24) == [2, 2]


def test_should_check_when_cat_and_dog_year_is_equal_27():
    assert get_human_age(27, 27) == [2, 2]


def test_should_check_when_cat_year_is_equal_28():
    assert get_human_age(28, 28) == [3, 2]


def test_should_check_when_dog_year_is_equal_29():
    assert get_human_age(29, 29) == [3, 3]


def test_should_check_when_cat_and_dog_year_is_equal_100():
    assert get_human_age(100, 100) == [21, 17]
