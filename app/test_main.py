from app.main import get_human_age


def test_should_return_0_when_age_is_less_15():
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_when_age_is_less_23():
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_when_age_is_less_27():
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_correct_list_when_age_is_over_27():
    assert get_human_age(100, 100) == [21, 17]
