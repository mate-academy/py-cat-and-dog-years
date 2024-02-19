from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0],
                     id="value check is null"),
        pytest.param(14, 14, [0, 0],
                     id="value check is 14"),
        pytest.param(15, 15, [1, 1],
                     id="value check is 15"),
        pytest.param(23, 23, [1, 1],
                     id="value check is 23"),
        pytest.param(24, 24, [2, 2],
                     id="value check is 24"),
        pytest.param(27, 27, [2, 2],
                     id="value check is 27"),
        pytest.param(28, 28, [3, 2],
                     id="value check is 28"),
        pytest.param(100, 100, [21, 17],
                     id="value check is 100"),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (f"Cat years {cat_age} "
        f"and Dog years {dog_age} "
        f"should be equal to {result}")
