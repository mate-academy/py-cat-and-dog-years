import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (10, 10, [0, 0]),
        (15, 15, [1, 1]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(
        cat_age,
        dog_age,
        result
) -> None:
    assert get_human_age(cat_age, dog_age) == result
