from app.main import get_human_age


def test_different_between_the_same_animals_age() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_negative_values() -> None:
    assert get_human_age(-1, -1) == [0, 0]


def test_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]
