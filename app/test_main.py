import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (27, 27, [2, 2]),
        (0, 0, [0, 0]),
        (28, 28, [3, 2]),
        (22, 12, [1, 0])
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
