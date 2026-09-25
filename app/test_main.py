from app.main import get_human_age


def test_should_return_zero_zer_when_ages_are_zero() -> None:
    result = get_human_age(0, 0)
    assert result == [0, 0]


def test_should_return_zero_zero_when_ages_are_below_fifteen() -> None:
    new_result = get_human_age(14, 14)
    assert new_result == [0, 0]


def test_should_return_one_one_when_ages_are_fifteen() -> None:
    number = get_human_age(15, 15)
    assert number == [1, 1]


def test_should_return_one_one_when_ages_are_twenty_three() -> None:
    new_number = get_human_age(23, 23)
    assert new_number == [1, 1]


def test_should_return_two_two_then_ages_are_twenty_four() -> None:
    numbers = get_human_age(24, 24)
    assert numbers == [2, 2]


def test_should_return_two_two_when_ages_are_twenty_seven() -> None:
    new_numbers = get_human_age(27, 27)
    assert new_numbers == [2, 2]


def test_should_return_three_two_when_ages_are_twenty_eight() -> None:
    results = get_human_age(28, 28)
    assert results == [3, 2]


def test_should_return_twenty_one_seventeen_when_ages_are_hundred() -> None:
    new_results = get_human_age(100, 100)
    assert new_results == [21, 17]
