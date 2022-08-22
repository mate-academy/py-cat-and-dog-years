from app.main import get_human_age


def test_check_zero_cat_and_dog_years():
    goals = get_human_age(0, 0)

    assert goals == [0, 0]


def test_check_cat_and_dog_14_years():
    goals = get_human_age(14, 14)

    assert goals == [0, 0]


def test_check_cat_and_dog_15_years():
    goals = get_human_age(15, 15)

    assert goals == [1, 1]


def test_check_car_and_dog_23_years():
    goals = get_human_age(23, 23)

    assert goals == [1, 1]


def test_check_cat_and_dog_24_years():
    goals = get_human_age(24, 24)

    assert goals == [2, 2]


def test_check_cat_and_dog_27_years():
    goals = get_human_age(27, 27)

    assert goals == [2, 2]


def test_check_cat__and_dog_28_years():
    goals = get_human_age(28, 28)

    assert goals == [3, 2]


def test_check_cat__and_dog_100_years():
    goals = get_human_age(100, 100)

    assert goals == [21, 17]
