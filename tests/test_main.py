from app.main import get_human_age


def test_right_convert_in_human_age():
    assert get_human_age(100, 100) == [21, 17]  # checking the differences between large numbers
    assert get_human_age(28, 28) == [3, 2]      # checking the differences between low numbers
    assert get_human_age(14, 14) == [0, 0]      # checking when age is under 15
    assert get_human_age(15, 24) == [1, 2]


def test_if_age_in_function_equal_to_0():
    assert get_human_age(0, 0) == [0, 0]
