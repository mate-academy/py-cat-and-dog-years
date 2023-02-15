import pytest

from app.main import get_human_age


def test_normal():
    assert get_human_age(28, 28) == [3, 2]


def test_type_error():
    with pytest.raises(TypeError):
        get_human_age("28", "28")

# def test_float_input():
#     assert get_human_age(28.1, 28) == [3, 2]
