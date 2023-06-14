import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0], id="both ages zero"),
        pytest.param(14, 14, [0, 0], id="both ages below 15"),
        pytest.param(23, 23, [1, 1], id="both ages between 15 and 24"),
        pytest.param(27, 27, [2, 2], id="both ages between 24 and 28"),
        pytest.param(28, 28, [3, 2], id="cat age greater than dog age"),
        pytest.param(100, 100, [21, 17], id="both ages greater than 28"),
        pytest.param(15, 0, [1, 0], id="cat equal to 15, dog below 15"),
        pytest.param(0, 15, [0, 1], id="cat below 15, dog age to 15"),
        pytest.param(10**10, 10**20, [2499999996, 19999999999999999997],
                     id="big numbers"),
        pytest.param(25, -50, [2, 0], id="negative dog age"),
        pytest.param(-2, 35, [0, 4], id="negative cat age"),
        pytest.param(-2, -1, [0, 0], id="both negative age"),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected
