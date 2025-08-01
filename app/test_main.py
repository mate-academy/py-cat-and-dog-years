from app.main import get_human_age


def test_zero_cat_and_dog_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_big_numbers_of_age() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_boundary_numbers_of_age() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(23, 23) == [1, 1]
