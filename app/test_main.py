import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "dog_age,cat_age,expected",
    [
        pytest.param(0, 0, [0, 0], id="Min age"),
        pytest.param(14, 14, [0, 0], id="Just below first threshold"),
        pytest.param(15, 15, [1, 1], id="First human year"),
        pytest.param(23, 23, [1, 1], id="Just below second threshold"),
        pytest.param(24, 24, [2, 2], id="second human year"),
        pytest.param(28, 28, [3, 2], id="Different age for cat & dog"),
        pytest.param(100, 100, [21, 17], id="Large age values"),
    ]
)
def test_get_human_age(dog_age: int, cat_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
