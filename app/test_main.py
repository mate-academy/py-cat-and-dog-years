import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0], id="Zero years"),
        pytest.param(14, 14, [0, 0], id="Less than 15 years"),
        pytest.param(15, 15, [1, 1], id="15 years"),
        pytest.param(23, 23, [1, 1], id="Less than 24 years"),
        pytest.param(24, 24, [2, 2], id="24 years"),
        pytest.param(27, 27, [2, 2], id="Less than 28 years"),
        pytest.param(28, 28, [3, 2], id="28 years"),
        pytest.param(100, 100, [21, 17], id="100 years")
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
