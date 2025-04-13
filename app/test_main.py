import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat,dog,result",
    [
        pytest.param(0, 0, [0, 0], id="cat and dog age are zero"),
        pytest.param(14, 14, [0,0], id="zero human year"),
        pytest.param(23, 23, [1, 1], id="one human year"),
        pytest.param(24, 24, [2, 2], id="two human years"),
        pytest.param(28, 29, [3, 3], id="three human years"),
        pytest.param(100, 100, [21, 17], id="big numbers")
    ]
)
def test_get_human_age(cat: int, dog: int, result: list) -> None:
    assert get_human_age(cat, dog) == result
