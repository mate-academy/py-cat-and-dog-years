import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,result",
    [
        pytest.param(0, 0, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(27, 27, [2, 2]),
        pytest.param(28, 28, [3, 2]),
        pytest.param(100, 100, [21, 17]),
    ]
)
def test_age_calculation(cat: int, dog: int,
                         result: list) -> None:
    assert (get_human_age(cat, dog) == result), \
        "not expected result"
