import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0], id="zero ages"),
        pytest.param(14, 14, [0, 0], id="below first threshold"),
        pytest.param(15, 15, [1, 1], id="first threshold"),
        pytest.param(23, 23, [1, 1], id="below second threshold"),
        pytest.param(24, 24, [2, 2], id="second threshold"),
        pytest.param(27, 27, [2, 2], id="below third threshold"),
        pytest.param(28, 28, [3, 2], id="third threshold for cat"),
        pytest.param(100, 100, [21, 17], id="big values"),
    ]
)
def test_get_human_age(
        cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected
