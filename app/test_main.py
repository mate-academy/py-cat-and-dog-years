from app.main import get_human_age


def test_return_list_with_zeros_if_both_animals_have_zero_age() -> None:
    assert get_human_age(0, 0) == [0 , 0]


def test_regular_calculation_check_of_the_function() -> None:
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(32, 39) == [4, 5]
