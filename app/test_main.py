from app.main import get_human_age


def test_should_return_valid_list() -> None:
    result = get_human_age(100, 100)

    assert result == [21, 17]


def test_should_return_zero_if_the_animal_age_under_fifteen() -> None:
    result = get_human_age(14, 14)

    assert result == [0, 0]


def test_age_should_be_one_when_animal_older_fourteen() -> None:
    result = get_human_age(23, 23)

    assert result == [1, 1]


def test_age_should_be_two_when_animal_older_twenty_three() -> None:
    result = get_human_age(27, 27)

    assert result == [2, 2]


def test_cat_age_should_be_three_when_animal_older_twenty_four() -> None:
    result = get_human_age(28, 28)

    assert result == [3, 2]
