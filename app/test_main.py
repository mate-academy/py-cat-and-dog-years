import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [pytest.param(
        0,
        0,
        [0, 0],
        id="pet age is 0"
    ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="pet age is less then 1 human year"
    ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="pet age is 1 human year"
    ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="pet age is more then 1 but less then 2 human years"
    ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="pet age = 2 human years"
    ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="equal pet age"
    ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="different pet age"
    ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="old pet age"
    ),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
