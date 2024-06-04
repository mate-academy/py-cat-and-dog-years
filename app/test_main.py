import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "input1, input2, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(
        input1: int, input2: int, expected_result: list
) -> None:
    assert (
        get_human_age(input1, input2) == expected_result
    ), f"get_human_age({input1}, {input2}) should return {expected_result}"


def test_get_human_age_exceptions() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", "2")
