import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,result",
    [
        pytest.param(0, 0, [0, 0], id="0 human"),
        pytest.param(15, 15, [1, 1], id="1 human"),
        pytest.param(23, 23, [1, 1], id="1 human"),
        pytest.param(23, 23, [1, 1], id="1 human"),
        pytest.param(28, 29, [3, 3], id="3 human"),
        pytest.param(31, 33, [3, 3], id="3 human"),
        pytest.param(32, 34, [4, 4], id="4 human")
    ]
)
def test_can_sum(cat: int, dog: int, result: list) -> None:
    assert (
        get_human_age(cat, dog) == result
    ), f"Result '{get_human_age(cat, dog)}' should be equal to '{result}'"
