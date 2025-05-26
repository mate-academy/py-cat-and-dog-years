from app.main import get_human_age
import pytest


@pytest.mark.paramertize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="cat and dog ages equal 0"),
        pytest.param(14, 14, [0, 0], id="cat and dog ages equal 14"),
        pytest.param(15, 15, [1, 1], id="cat and dog ages equal 15"),
        pytest.param(24, 24, [2, 2], id="cat and dog ages equal 24"),
        pytest.param(28, 28, [3, 2], id="cat and dog ages equal 28"),
        pytest.param(100, 100, [21, 17], id="cat and dog ages equal 100")
    ]
)

def test_get_human_age(cat_age, dog_age, result) -> None:
    assert get_human_age(cat_age, dog_age) == result
