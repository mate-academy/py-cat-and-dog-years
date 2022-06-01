import pytest

from app.main import get_human_age


@pytest.mark.parametrize("arg1, arg2", [(15, 15), ])
def test_type_return_get_human_age(arg1, arg2):
    assert isinstance(get_human_age(arg1, arg2), list)


@pytest.mark.parametrize("arg1, arg2", [(15, 15), ])
def test_len_list_return_get_human_age(arg1, arg2):
    assert len(get_human_age(arg1, arg2)) == 2


@pytest.mark.parametrize("args", [(15, 15)])
def test_type_return_value_in_list_get_human_age(args):
    f = True
    for i in range(len(get_human_age(*args))):
        f = isinstance(get_human_age(*args)[i], int)
    assert f


@pytest.mark.parametrize(
    "args, result",
    [
        ((0, 0), [0, 0]),
        ((14, 14), [0, 0]),
        ((15, 15), [1, 1]),
        ((23, 23), [1, 1]),
        ((24, 24), [2, 2]),
        ((27, 27), [2, 2]),
        ((28, 28), [3, 2]),
        ((100, 100), [21, 17])
    ]
)
def test_get_human_age(args, result):
    assert get_human_age(*args) == result
