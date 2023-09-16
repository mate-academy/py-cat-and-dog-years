from app.main import get_human_age


def test_check_cat_dog_age_equal_zero() -> None:
    assert get_human_age(cat_age=0, dog_age=0) == [0, 0]


def test_check_get_human_age_return_list() -> None:
    assert isinstance(get_human_age(cat_age=10, dog_age=10), list)


def test_check_age_if_cat_dog_age_equal_tw_eight() -> None:
    assert get_human_age(cat_age=28, dog_age=28) == [3, 2]
