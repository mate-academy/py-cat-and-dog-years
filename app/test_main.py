import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0], id="zero_years"),
        pytest.param(14, 14, [0, 0], id="less_than_15_years"),
        pytest.param(15, 15, [1, 1], id="one_human_age"),
        pytest.param(23, 23, [1, 1], id="one_human_age"),
        pytest.param(24, 24, [2, 2], id="twp_human_age"),
        pytest.param(27, 27, [2, 2], id="twp_human_age"),
        pytest.param(28, 28, [3, 2], id="two_human_age"),
        pytest.param(100, 100, [21, 17], id="big_human_age")
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
