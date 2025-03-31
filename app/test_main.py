import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 14, [0, 0]),
        (15, 23, [1, 1]),
        (27, 28, [2, 2]),
        (100, 100, [21, 17]),
        (-13, -256, [0, 0]),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected, (
        f"Failed for input: cat_age={cat_age}, dog_age={dog_age}"
    )
