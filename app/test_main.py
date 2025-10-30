import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0, 0, [0, 0], id="return zero if age is smaller 15"
        ),
        pytest.param(
            14, 14, [0, 0], id="return zero if age is smaller 15"
        ),
        pytest.param(
            15, 15, [1, 1], id="return 1 if 15<=age<=23"
        ),
        pytest.param(
            23, 23, [1, 1], id="return 1 if 15<=age<=23"
        ),
        pytest.param(
            24, 24, [2, 2], id="return 2 if 24<=age<=27"
        ),
        pytest.param(
            27, 27, [2, 2], id="return 2 if 24<=age<=27"
        ),
        pytest.param(
            28, 28, [3, 2], id="return cat is older if age>=28"
        ),
        pytest.param(
            100, 100, [21, 17], id="return cat is older if age>28"
        ),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
