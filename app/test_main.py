from app.main import get_human_age


def test_should_return_a_list_with_the_same_age_of_cat_and_dog() -> None:
    goals = get_human_age(27, 27)
    assert goals == [2, 2]


def test_should_return_a_list_with_the_different_age_of_cat_and_dog() -> None:
    goals = get_human_age(100, 100)
    assert goals == [21, 17]
