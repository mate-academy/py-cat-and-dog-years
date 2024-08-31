from app.main import get_human_age
import pytest


def test_the_output_has_to_be_equal_to_expected() -> None:
    assert get_human_age(0, 0) == [0, 0], "Fix your code"
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]


def test_the_output_has_to_be_integer() -> None:
    with pytest.raises(TypeError):
        assert isinstance(get_human_age("Bob", 24)[1], int)
        assert isinstance(get_human_age("24", 24)[0], int)


def test_negative_or_large_numbers() -> None:
    assert get_human_age(-1, 2) == [0, 0]
