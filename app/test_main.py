import pytest

from app.main import get_human_age


@pytest.mark.parametrize("input_params, expected_output", [
    ((0, 0), [0, 0]),
    ((14, 14), [0, 0]),
    ((15, 15), [1, 1]),
    ((23, 23), [1, 1]),
    ((24, 24), [2, 2]),
    ((27, 27), [2, 2]),
    ((28, 28), [3, 2]),
    ((100, 100), [21, 17]),
    ((-15, -15), [0, 0])
])
def test_get_human_age(
        input_params: tuple[int, int],
        expected_output: list[int]
) -> None:
    assert get_human_age(*input_params) == expected_output


def test_get_human_age_invalid_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", "15")
