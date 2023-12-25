import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="zero years test "),
        pytest.param(14, 14, [0, 0], id="less than 15 years test"),
        pytest.param(15, 15, [1, 1], id="15 years test"),
        pytest.param(23, 23, [1, 1], id="23 years test"),
        pytest.param(24, 24, [2, 2], id="24 years test"),
        pytest.param(27, 27, [2, 2], id="27 years test"),
        pytest.param(28, 28, [3, 2], id="28 years test"),
        pytest.param(100, 100, [21, 17], id="centenary test"),
    ],

)
def test_can_sum(cat_age: int | str,
                 dog_age: int | str,
                 result: int | str,
                 ) -> None:
    assert get_human_age(cat_age, dog_age) == result
