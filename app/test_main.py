import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (1, 1, [0, 0]),
        (16, 16, [1, 1]),
        (27, 28, [2, 2]),
        (32, 34, [4, 4]),
        (28, 39, [3, 5]),
        (23, 23, [1, 1]),
        (14, 14, [0, 0])
    ]
)


def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
