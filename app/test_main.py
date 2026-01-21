from app.main import get_human_age
import pytest


@pytest.mark.parametrize("ages, result", [
    ((0, 0), [0, 0]),
    ((14, 14), [0, 0]),
    ((15, 15), [1, 1]),
    ((23, 7), [1, 0]),
    ((12, 20), [0, 1]),
    ((25, 26), [2, 2]),
    ((28, 28), [3, 2]),
    ((50, 50), [8, 7]),
])
def test(ages: tuple, result: list) -> None:
    assert get_human_age(*ages) == result
