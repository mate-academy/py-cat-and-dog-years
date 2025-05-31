from app.main import get_human_age


def test_should_return_list() -> None:
    assert type(get_human_age(15, 15)) == list


def test_should_return_list_with_two_elements() -> None:
    assert len(get_human_age(15, 15)) == 2


def test_should_return_zeros_if_animal_is_too_young() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_result_with_2_integers() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_calculate_correctly_for_cat_and_dog() -> None:
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(29, 29) == [3, 3]
