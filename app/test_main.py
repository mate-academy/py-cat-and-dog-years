from app.main import get_human_age


def test_should_return_zero_when_input_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_input_negative_values() -> None:
    assert get_human_age(-5, 1) == [0, 0]
    assert get_human_age(5, -1) == [0, 0]


def test_should_convert_animal_years_younger_than_1_human() -> None:
    assert get_human_age(12, 14) == [0, 0]


def test_should_convert_15_animals_to_1_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_verify_increase_on_1_more_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_convert_extra_cat_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_convert_extra_dog_years() -> None:
    assert get_human_age(16, 29) == [1, 3]


def test_incorrect_type_of_data() -> None:
    try:
        get_human_age("28", [28])
    except TypeError as e:
        assert "'<' not supported between instances of 'str' and 'int'"
