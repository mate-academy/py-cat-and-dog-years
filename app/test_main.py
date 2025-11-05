from app.main import get_human_age


def test_should_return_zero_for_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_for_first_year_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_for_second_year_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_three_when_cat_exceeds_second_threshold() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_large_correct_values() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_should_return_correct_values_for_random_cases() -> None:
    assert get_human_age(29, 29) == [3, 3]
    assert get_human_age(35, 40) == [4, 5]
    assert get_human_age(50, 55) == [8, 8]
    assert get_human_age(60, 70) == [11, 11]
    assert get_human_age(90, 95) == [18, 16]


def test_monotonic_increase_of_human_years() -> None:
    previous_cat, previous_dog = 0, 0
    for age in range(0, 101):
        cat, dog = get_human_age(age, age)
        assert cat >= previous_cat
        assert dog >= previous_dog
        previous_cat, previous_dog = cat, dog
