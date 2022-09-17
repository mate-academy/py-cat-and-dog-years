from app.main import get_human_age


def test_should_return_correct_result_if_ages_bigger_then_14():
    cat_age, dog_age = 28, 28
    assert get_human_age(cat_age, dog_age) == [3, 2]


def test_should_return_correct_result_if_cat_age_smaller_then_15():
    cat_age, dog_age = 11, 15
    assert get_human_age(cat_age, dog_age) == [0, 1]


def test_should_return_correct_result_if_dog_age_smaller_then_15():
    cat_age, dog_age = 15, 10
    assert get_human_age(cat_age, dog_age) == [1, 0]


def test_should_return_zeros_if_ages_are_negative():
    cat_age, dog_age = -1, -12
    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_should_return_correct_result_with_big_numbers():
    cat_age, dog_age = 340, 280
    assert get_human_age(cat_age, dog_age) == [81, 53]
