import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="test zeroes"),
        pytest.param(14, 14, [0, 0], id="test value between 0 and 15"),
        pytest.param(15, 15, [1, 1], id="test 15 years"),
        pytest.param(24, 24, [2, 2], id="test 24 years (15 plus 9)"),
        pytest.param(28, 28, [3, 2],
                     id="test the difference after second human year"),
        # pytest.param(31.8, 33.5, [3, 3], id="test floats"),
    ]
)
def test_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert (get_human_age(cat_age, dog_age) == result
            ), (f"Converting of {cat_age} cat age and "
                f"{dog_age} dog age should be equal to "
                f"{result}")
