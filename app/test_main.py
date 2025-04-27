from app.main import get_human_age


def test_should_return_0_when_animal_age_less_then_first_year() -> None:
    result = get_human_age(14, 14)

    assert result == [0, 0]


def test_should_return_1_when_animal_age_more_then_first_year() -> None:
    result = get_human_age(15, 15)

    assert result == [1, 1]


def test_should_return_2_when_animal_age_more_then_second_year() -> None:
    result = get_human_age(24, 24)

    assert result == [2, 2]


def test_should_return_3_when_cat_age_more_then_each_year() -> None:
    result = get_human_age(28, 28)

    assert result == [3, 2]


def test_should_return_true_res_when_animal_age_more_then_each_year() -> None:
    result = get_human_age(100, 100)

    assert result == [21, 17]
