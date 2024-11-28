import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
    ]
)
def test_for_human_years(cat: int, dog: int, result: list) -> None:
    assert get_human_age(cat, dog) == result
