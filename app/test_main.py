from app.main import get_human_age


def test_zero_ages():
    ages = {"cat_age": 14, "dog_age": 14, "human_age": [0, 0]}
    assert get_human_age(
        ages["cat_age"], ages["dog_age"]) == ages["human_age"]


def test_first_ages():
    ages = {"cat_age": 15, "dog_age": 15, "human_age": [1, 1]}
    assert get_human_age(
        ages["cat_age"], ages["dog_age"]) == ages["human_age"]


def test_second_ages():
    ages = {"cat_age": 24, "dog_age": 24, "human_age": [2, 2]}
    assert get_human_age(
        ages["cat_age"], ages["dog_age"]) == ages["human_age"]


def test_more_ages():
    ages = {"cat_age": 28, "dog_age": 29, "human_age": [3, 3]}
    assert get_human_age(
        ages["cat_age"], ages["dog_age"]) == ages["human_age"]


def test_result_should_is_list():
    assert isinstance(get_human_age(10, 10), list)
