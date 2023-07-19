from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="get_from_zeroes"),
        pytest.param(14, 14, [0, 0], id="get_zeroes_from_positive"),
        pytest.param(15, 15, [1, 1], id="get_ones"),
        pytest.param(23, 23, [1, 1], id="get_ones_from_the_biggest"),
        pytest.param(24, 24, [2, 2], id="get_two_from_smallest"),
        pytest.param(27, 27, [2, 2], id="get_two_from_biggest"),
        pytest.param(28, 27, [3, 2], id="get_three_for_cat"),
        pytest.param(100, 100, [21, 17], id="test_hundreds")
    ]
)
def test_get_result(cat_age: int, dog_age: int, result: list[str]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), f"Get human age of {cat_age} and {dog_age} should be equal to {result}"
