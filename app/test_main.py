import app.main as main


def test_return_0_when_age_is_less_15() -> None:
    assert main.get_human_age(14, 14) == [0, 0]


def test_return_1_when_age_is_15() -> None:
    assert main.get_human_age(15, 15) == [1, 1]


def test_return_1_before_24() -> None:
    assert main.get_human_age(23, 23) == [1, 1]


def test_return_2_when_age_is_24() -> None:
    assert main.get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_calculated_differently_after_24() -> None:
    assert main.get_human_age(28, 28) == [3, 2]


def test_work_with_big_age() -> None:
    assert main.get_human_age(100, 100) == [21, 17]


def test_calculated_cat_and_dog_separately() -> None:
    assert main.get_human_age(29, 28) == [3, 2]
