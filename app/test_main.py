import pytest

from app.main import get_human_age


@pytest.mark.parametrize("value,result",
                         [((14, 14), [0, 0]),
                          ((15, 15), [1, 1]),
                          ((24, 24), [2, 2]),
                          ((28, 28), [3, 2]),
                          ((100, 100), [21, 17])])
def test_usual_case(value: tuple, result: list) -> None:
    assert get_human_age(*value) == result


@pytest.mark.parametrize("value",
                         [(0, 0),
                          (-1, -1),
                          (0, 0.2),
                          (0, True)])
def test_data_out_of_normal_range(value: tuple) -> None:
    assert get_human_age(*value) == [0, 0]


@pytest.mark.parametrize("value",
                         [(1, "hh"),
                          (1, []),
                          (2, {}),
                          (1, ())])
def test_wrong_type(value: tuple) -> None:
    try:
        get_human_age(*value)
    except TypeError:
        pass
