from app import main


def test_zero_age() -> None:
    assert main.get_human_age(0, 0) == [0, 0]


def test_before_first_year() -> None:
    assert main.get_human_age(14, 14) == [0, 0]


def test_exactly_first_year() -> None:
    assert main.get_human_age(15, 15) == [1, 1]


def test_before_second_year() -> None:
    assert main.get_human_age(23, 23) == [1, 1]


def test_exactly_second_year() -> None:
    assert main.get_human_age(24, 24) == [2, 2]


def test_before_cat_extra_year() -> None:
    assert main.get_human_age(27, 28) == [2, 2]


def test_cat_gets_extra_year() -> None:
    assert main.get_human_age(28, 28) == [3, 2]


def test_dog_gets_extra_year() -> None:
    assert main.get_human_age(28, 29) == [3, 3]


def test_large_values() -> None:
    assert main.get_human_age(100, 100) == [21, 17]


def test_return_length() -> None:
    result = main.get_human_age(50, 50)
    assert len(result) == 2
