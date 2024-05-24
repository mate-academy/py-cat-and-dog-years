import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_to_human, dog_to_human, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_to_human: int,
                       dog_to_human: int,
                       expected: list) -> None:
    assert get_human_age(cat_to_human, dog_to_human) == expected
