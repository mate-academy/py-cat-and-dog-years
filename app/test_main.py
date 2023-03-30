from app.main import get_human_age


def test_should_return_zero() -> None:
    cat_age = 12
    dog_age = 12
    actually_result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    expected_result = [0, 0]
    assert actually_result == expected_result


def test_should_return_one_years() -> None:
    cat_age = 15
    dog_age = 23
    actually_result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    expected_result = [1, 1]
    assert actually_result == expected_result


def test_should_return_two_and_three_years_respectively() -> None:
    cat_age = 27
    dog_age = 30
    actually_result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    expected_result = [2, 3]
    assert actually_result == expected_result


def test_should_return_21_and_17_years_respectively() -> None:
    cat_age = 100
    dog_age = 100
    actually_result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    expected_result = [21, 17]
    assert actually_result == expected_result
