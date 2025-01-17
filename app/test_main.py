from app.main import get_human_age


def test_should_return_array() -> None:
    human_age = get_human_age(5, 10)
    assert isinstance(human_age, list)


def test_result_array_should_have_two_elements() -> None:
    human_age = get_human_age(5, 10)
    assert len(human_age) == 2


def test_elements_in_array_should_be_integers() -> None:
    human_age = get_human_age(5, 10)
    assert (isinstance(human_age[0], int) and isinstance(human_age[1], int))


def test_zero_values() -> None:
    human_age = get_human_age(0, 0)
    assert human_age == [0, 0]


def test_age_less_than_15_should_return_zero() -> None:
    human_age = get_human_age(14, 14)
    assert human_age == [0, 0]


def test_age_15_should_return_1() -> None:
    human_age = get_human_age(15, 15)
    assert human_age == [1, 1]


def test_age_less_than_24_should_return_1() -> None:
    human_age = get_human_age(23, 23)
    assert human_age == [1, 1]


def test_age_24_and_more_should_return_2() -> None:
    human_age = get_human_age(24, 24)
    assert human_age == [2, 2]


def test_every_4_cat_and_every_5_dog_years_should_add_1() -> None:
    human_age = get_human_age(28, 28)
    assert human_age == [3, 2]


def test_100_years() -> None:
    human_age = get_human_age(100, 100)
    assert human_age == [21, 17]
