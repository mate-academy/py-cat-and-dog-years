from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_age",
    [
        pytest.param(0, 0, [0, 0], id="Age of human = 0"),
        pytest.param(15, 15, [1, 1], id="Age of human = 1"),
        pytest.param(28, 28, [3, 2], id="Age of human = 3, 2 years"),
        pytest.param(100, 100, [21, 17], id="Age of human = 21 and 17 years old"),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age
