from app.main import get_human_age


def test_should_return_zeros_when_age_0_14():
    human_age = get_human_age(14, 14)
    assert human_age == [0, 0]


def test_should_return_1_when_age_15_23():
    human_age = get_human_age(23, 23)
    assert human_age == [1, 1]


def test_should_return_2_when_age_24_27():
    human_age = get_human_age(27, 27)
    assert human_age == [2, 2]


def test_should_return_list_when_age_over_27():
    human_age = get_human_age(100, 100)
    assert human_age == [21, 17]
