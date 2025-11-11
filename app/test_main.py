import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0], id="both_zero"),
        pytest.param(14, 14, [0, 0], id="below_threshold"),
        pytest.param(15, 15, [1, 1], id="first_threshold"),
        pytest.param(23, 23, [1, 1], id="just_above_first_threshold"),
        pytest.param(24, 24, [2, 2], id="second_threshold"),
        pytest.param(27, 27, [2, 2], id="between_second_and_third"),
        pytest.param(28, 28, [3, 2], id="third_threshold"),
        pytest.param(100, 100, [21, 17], id="large_numbers"),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
