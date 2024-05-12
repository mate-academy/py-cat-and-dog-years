from app.main import get_human_age


def test_should_return_0_year_cat_and_dog() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_year_cat_and_0_year_dog() -> None:
    assert get_human_age(16, 9) == [1, 0]


def test_should_return_0_year_cat_and_1_year_dog() -> None:
    assert get_human_age(8, 17) == [0, 1]


def test_should_return_1_year_cat_and_dog() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_2_year_cat_and_dog() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_3_year_cat_and_dog() -> None:
    assert get_human_age(30, 31) == [3, 3]


def test_should_return_4_year_cat_and_3_year_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]