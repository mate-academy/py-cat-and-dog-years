from app.main import get_human_age


def test_return_list() -> None:
    assert isinstance(get_human_age(3, 4), list)


def test_cat_and_dog_age_convert_to_human_age() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_zero_value_in_function() -> None:
    assert get_human_age(0, 0) == [0, 0]

