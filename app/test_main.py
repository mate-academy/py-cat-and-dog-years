import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "a,b,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17])
    ]
)
def test_animal_age_vs_human(a: int, b: int, result: list[int]) -> None:
    assert (get_human_age(a, b) == result)
