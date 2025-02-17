from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(4, 4, [0, 0], id="When pets ages = 0"),
        pytest.param(16, 16, [1, 1], id="When pets ages = 1"),
        pytest.param(24, 24, [2, 2], id="When pets ages = 2"),
        pytest.param(28, 28, [3, 2], id="When cat's getting older than dogs"),
        pytest.param(-15, 15, [0, 1], id="When one of ages is negative"),
        pytest.param(0, 15, [0, 1], id="When one of ages = 0"),
        pytest.param(1000, 1000, [246, 197], id="When ages are large numbers"),
    ]
)
def test_pets_ages(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
