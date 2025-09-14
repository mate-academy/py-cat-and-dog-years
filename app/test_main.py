from app.main import get_human_age


def test_animal_age_0_0_to_convert_human_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_animal_age_14_14_to_convert_human_age() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_animal_age_15_15_to_convert_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_animal_age_23_23_to_convert_human_age() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_animal_age_24_24_to_convert_human_age() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_animal_age_27_27_to_convert_human_age() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_animal_age_28_28_to_convert_human_age() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_animal_age_100_100_to_convert_human_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
