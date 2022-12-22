from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "example_input, expected",
    [
        (get_human_age(0, 0), [0, 0]),
        (get_human_age(14, 14), [0, 0]),
        (get_human_age(15, 15), [1, 1]),
        (get_human_age(23, 23), [1, 1]),
        (get_human_age(24, 24), [2, 2]),
        (get_human_age(27, 27), [2, 2]),
        (get_human_age(28, 28), [3, 2]),
        (get_human_age(100, 100), [21, 17])
    ]
)
def test_get_human_age(example_input: list, expected: list) -> None:
    assert example_input == expected
