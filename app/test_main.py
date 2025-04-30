from app.main import get_human_age


def test_should_return_zero_for_animals_younger_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]

def test_should_return_one_for_exactly_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]

def test_should_return_two_for_exactly_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]

def test_should_add_extra_years_for_cat_after_24_by_fours() -> None:
    assert get_human_age(32, 24) == [4, 2]

def test_should_add_extra_years_for_dog_after_24_by_fives() -> None:
    assert get_human_age(24, 37) == [2, 4]

def test_should_return_correct_values_for_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]

def test_should_return_array_of_two_elements() -> None:
    assert len(get_human_age(100, 100)) == 2
