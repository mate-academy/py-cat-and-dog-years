from app.main import get_human_age


def test_cat_dog_age_must_be_0_when_under_15() -> None:
    assert get_human_age(13, 13) == [0, 0]


def test_cat_dog_age_must_be_1_when_under_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_dog_age_must_be_1_next_years() -> None:
    assert get_human_age(28, 28) == [3, 2]
