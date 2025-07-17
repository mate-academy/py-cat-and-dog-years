from app.main import get_human_age


def test_cat_age_should_return_0_when_less_than_15() -> None:
    assert get_human_age(14, 0)[0] == 0


def test_cat_age_should_return_1_when_between_15_and_24_inclusive() -> None:
    assert get_human_age(15, 0)[0] == 1


def test_cat_age_should_return_2_when_between_25_and_27() -> None:
    assert get_human_age(25, 0)[0] == 2


def test_cat_age_should_return_3_when_exactly_28() -> None:
    assert get_human_age(28, 0)[0] == 3


def test_cat_age_should_return_correct_value_for_large_age() -> None:
    assert get_human_age(100, 0)[0] == 21


def test_dog_age_should_return_0_when_less_than_15() -> None:
    assert get_human_age(0, 14)[1] == 0


def test_dog_age_should_return_1_when_between_15_and_24_inclusive() -> None:
    assert get_human_age(0, 15)[1] == 1


def test_dog_age_should_return_2_when_between_25_and_28() -> None:
    assert get_human_age(0, 26)[1] == 2


def test_dog_age_should_return_3_when_exactly_29() -> None:
    assert get_human_age(0, 29)[1] == 3


def test_dog_age_should_return_correct_value_for_large_age() -> None:
    assert get_human_age(0, 100)[1] == 17


def test_age_23_cat_and_dog_should_convert_into_1_human() -> None:
    assert get_human_age(23, 23) == [1, 1]
