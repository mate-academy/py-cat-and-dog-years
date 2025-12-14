import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0, 0], id="both_zero"),
        pytest.param(14, 14, [0, 0], id="both_before_15"),
        pytest.param(15, 15, [1, 1], id="both_at_15"),
        pytest.param(23, 23, [1, 1], id="both_before_24"),
        pytest.param(24, 24, [2, 2], id="both_at_24"),
        pytest.param(27, 27, [2, 2], id="both_between_24_and_next_step"),
        pytest.param(28, 28, [3, 2], id="cat_steps_at_28"),
        pytest.param(100, 100, [21, 17], id="both_large_ages"),
    ],
)
def test_get_human_age_threshold_cases(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(32, 34, [4, 4], id="independence_cat32_dog34"),
        pytest.param(40, 39, [6, 5], id="independence_cat40_dog39"),
    ],
)
def test_get_human_age_independence_cases(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
