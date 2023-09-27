from app.main import get_human_age


def test_value_zero_input_for_funtion() -> None:
    result = get_human_age(0, 0)
    assert result == [0, 0]


def test_for_big_values() -> None:
    result = get_human_age(100, 100)
    assert result[0] != result[1]
    assert result == [21, 17]


def test_second_value_is_less_then_first() -> None:
    result = get_human_age(28, 28)
    assert result[0] > result[1]


def test_can_take_two_different_values() -> None:
    result = get_human_age(15, 14)
    assert result == [1, 0]
