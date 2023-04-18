from app.main import get_human_age


def test_should_return_zeros_when_animals_ages_less_then_15() -> None:
    negative_values = get_human_age(-1, -2)
    zero_values = get_human_age(0, 0)
    max_positive = get_human_age(14, 14)

    assert negative_values == zero_values == max_positive == [0, 0]


def test_should_return_1_when_ages_more_than_14_and_no_extra_life() -> None:
    assert get_human_age(15, 15) == get_human_age(23, 23) == [1, 1]


def test_should_return_many_animals_extra_life() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_for_incorrect_input_types() -> None:
    try:
        get_human_age(None, None)
        get_human_age("text", "0")
        get_human_age([1], [0])
        get_human_age({1: 1}, {0: 0})
    except TypeError:
        pass
