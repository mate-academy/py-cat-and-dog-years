import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0, 0], id="Zero"),
        # pytest.param(15.3, 15.3, [1, 1], id="float value"),
        pytest.param(14, 14, [0, 0], id="higher bound 0"),
        pytest.param(15, 15, [1, 1], id="lower bound 1 year"),
        pytest.param(23, 23, [1, 1], id="higher bound 1 year"),
        pytest.param(24, 24, [2, 2], id="lower bound 2 years"),
        pytest.param(27, 28, [2, 2], id="bound between years"),
        pytest.param(28, 29, [3, 3], id="lower bound for 3 years"),
        pytest.param(1000, 1500, [246, 297], id="Huge values"),
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected: list) -> None:

    assert get_human_age(cat_age, dog_age) == expected
