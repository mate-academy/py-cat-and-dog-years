from app.main import get_human_age


def test_cat_age_conversion() -> None:

    assert get_human_age(5, 10) == [0, 0]

    assert get_human_age(15, 20) == [1, 1]

    assert get_human_age(30, 40) == [3, 5]


def test_dog_age_conversion() -> None:
    assert get_human_age(10, 5) == [0, 0]

    assert get_human_age(20, 21) == [1, 1]

    assert get_human_age(30, 35) == [3, 4]
