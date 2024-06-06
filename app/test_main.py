from app.main import get_human_age


def test_should_return_list_of_given_length() -> None:
    assert len(get_human_age(12, 23)) == 2


def test_should_return_list_elements_is_int() -> None:
    for element in get_human_age(12, 23):
        assert isinstance(element, int)


def test_should_return_try_value_if_younger_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_try_value_if_younger_24_and_older_15() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_try_value_if_cat_older_24() -> None:
    assert get_human_age(24, 12)[0] == 2
    assert get_human_age(28, 12)[0] == 3


def test_should_return_try_value_if_dog_older_25() -> None:
    assert get_human_age(24, 29)[1] == 3
