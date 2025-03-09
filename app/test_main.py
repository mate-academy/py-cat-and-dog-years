import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_ages",
    [
        pytest.param(0, 0, [0, 0], id="ages 0 should return 0 0"),
        pytest.param(14, 14, [0, 0], id="ages 14 should return 0 0"),
        pytest.param(15, 15, [1, 1], id="ages 15 should return 1 1"),
        pytest.param(20, 20, [1, 1], id="ages 20 should return 1 1"),
        pytest.param(23, 23, [1, 1], id="ages 23 should return 1 1"),
        pytest.param(27, 28, [2, 2], id="ages 27 28 should return 2 2"),
        pytest.param(28, 29, [3, 3], id="ages 28 29 should return 3 3"),
        pytest.param(30, 31, [3, 3], id="ages 30 31 should return 3 3"),
        pytest.param(32, 34, [4, 4], id="ages 32 34 should return 4 4"),
        pytest.param(100, 100, [21, 17], id="ages 100 should return 21 17"),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_ages: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_ages
