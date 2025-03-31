import pytest

from app.main import get_human_age


def test_type_return_get_human_age():
    assert isinstance(get_human_age(15, 15), list)


@pytest.mark.parametrize("args", [(15, 15), (0, 0)])
def test_type_return_value_in_list_get_human_age(args):
    assert all(isinstance(result, int) for result in get_human_age(*args))


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
