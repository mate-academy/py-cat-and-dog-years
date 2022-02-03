from app.main import get_human_age


def test_right_convert_in_human_age():
    assert get_human_age(100, 100) == [21, 17]  # checking the differences between large numbers
    assert get_human_age(28, 28) == [3, 2]  # checking the differences between low numbers


def test_if_age_in_function_equal_to_0():
    assert get_human_age(0, 0) == [0, 0]
