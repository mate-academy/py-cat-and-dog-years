import pytest

from app.main import get_human_age


def test_normal() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("28", "28")

# def test_float_input():
#     assert get_human_age(28.1, 28) == [3, 2]
