from app.main import get_human_age


def test_should_be_zero_animal_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_be_output_age_zero_human_age() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_be_output_age_one_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_be_output_age_one_human_age_too() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_be_output_age_two_human_age() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_be_output_age_three_human_age() -> None:
    assert get_human_age(28, 29) == [3, 3]
