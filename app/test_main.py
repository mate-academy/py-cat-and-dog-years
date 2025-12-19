import app.main as main


def test_should_return_zero_human_years_when_ages_are_zero() -> None:
    assert main.get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_age_is_less_than_first_threshold() -> None:
    assert main.get_human_age(14, 14) == [0, 0]


def test_should_convert_first_15_years_to_one_human_year() -> None:
    assert main.get_human_age(15, 15) == [1, 1]


def test_should_not_increase_human_years_until_second_threshold() -> None:
    assert main.get_human_age(23, 23) == [1, 1]


def test_should_convert_next_9_years_to_second_human_year() -> None:
    assert main.get_human_age(24, 24) == [2, 2]


def test_should_discard_remainder_years() -> None:
    assert main.get_human_age(27, 27) == [2, 2]


def test_should_convert_cat_and_dog_years_differently() -> None:
    assert main.get_human_age(28, 28) == [3, 2]


def test_should_correctly_convert_large_ages() -> None:
    assert main.get_human_age(100, 100) == [21, 17]


def test_should_work_with_different_ages_for_cat_and_dog() -> None:
    assert main.get_human_age(30, 15) == [3, 1]
    assert main.get_human_age(15, 30) == [1, 3]


def test_should_calculate_cat_years_correctly_after_second_threshold() -> None:
    assert main.get_human_age(28, 0)[0] == 3
    assert main.get_human_age(32, 0)[0] == 4


def test_should_calculate_dog_years_correctly_after_second_threshold() -> None:
    assert main.get_human_age(0, 29)[1] == 3
    assert main.get_human_age(0, 34)[1] == 4


def test_should_handle_edge_cases_correctly() -> None:
    assert main.get_human_age(24, 24) == [2, 2]
    assert main.get_human_age(28, 28) == [3, 2]
