from app.main import get_human_age


def test_should_return_list_with_animal_age_equal_0():
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_covert_age_when_animal_age_equal_15():
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_covert_age_when_animal_age_equal_24():
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_covert_age_when_animal_age_equal_29():
    assert get_human_age(29, 29) == [3, 3]


def test_should_return_covert_age_when_animal_age_big_digit():
    assert get_human_age(120, 99) == [26, 17]
