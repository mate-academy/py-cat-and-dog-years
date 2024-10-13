import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="should return zeros for zeros"),
        pytest.param(14, 14, [0, 0], id="should return zeros for if age less than 15"),
        pytest.param(15, 23, [1, 1], id="should return 1 in range 15-23"),
        pytest.param(27, 27, [2, 2], id="should return correct data fo 27, 27"),
        pytest.param(28, 28, [3, 2], id="should return correct data for 28, 28"),
        pytest.param(100, 100, [21, 17], id="should return correct data for 100, 100")
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int, int]):
    assert get_human_age(cat_age, dog_age) == result
