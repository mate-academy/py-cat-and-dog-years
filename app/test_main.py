from app.main import get_human_age


def test_convert_returns_0_for_age_below_first_year() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_convert_returns_1_for_age_below_first_plus_second_year() -> None:
    assert get_human_age(20, 20) == [1, 1]


def test_convert_returns_correct_value_for_age_above_two_years() -> None:
    assert get_human_age(29, 30) == [3, 3]


def test_convert_handles_exact_first_year_boundary() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_convert_handles_exact_second_year_boundary() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_convert_with_various_each_year_values() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_get_human_age_returns_list_of_two_values() -> None:
    result = get_human_age(10, 10)
    assert isinstance(result, list)
    assert len(result) == 2


def test_get_human_age_correctly_converts_cat_and_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_cat_zero_dog_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_with_large_ages() -> None:
    assert get_human_age(50, 50) == [8, 7]


def test_get_human_age_independent_calculations_for_cat_and_dog() -> None:
    assert get_human_age(29, 34) == [3, 4]
