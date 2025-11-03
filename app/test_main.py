from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(16, 16, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(55, 55, [9, 8]),
        pytest.param(66.6, 77.7, [12.0, 12.0]),
        pytest.param(100, 100, [21, 17])
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected: list[int]) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected

