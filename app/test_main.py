import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="both age zero"),
        pytest.param(14, 14, [0, 0], id="below 15"),
        pytest.param(15, 15, [1, 1], id="14 < age < 24"),
        pytest.param(27, 27, [2, 2], id="24 <= age <= 27"),
        pytest.param(28, 28, [3, 2], id="cat ages every 4 years, dog every 5"),
        pytest.param(100, 100, [21, 17], id="convert big number")
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
