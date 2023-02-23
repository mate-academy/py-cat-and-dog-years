import pytest

from app.main import get_human_age


@pytest.mark.parametrize("input_age, expected_output", [
    ((-1, -1), [0, 0]),
    ((0, 0), [0, 0]),
    ((14, 14), [0, 0]),
    ((15, 15), [1, 1]),
    ((23, 23), [1, 1]),
    ((24, 24), [2, 2]),
    ((28, 28), [3, 2]),
    ((100, 100), [21, 17])
])
def test_get_human_age(input_age, expected_output):
    assert get_human_age(*input_age) == expected_output


def test_raise_error_when_incorect_value() -> None:
    with pytest.raises(TypeError):
        get_human_age(2, "2")

