import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(0, 0, [0, 0], id="Human age up to a year"),
        pytest.param(14, 14, [0, 0], id="Human age up to a year"),
        pytest.param(15, 15, [1, 1], id="Human age up to two years"),
        pytest.param(23, 23, [1, 1], id="Human age up to two years"),
        pytest.param(24, 24, [2, 2], id="Human age is two years"),
        pytest.param(27, 27, [2, 2], id="Human age is two years"),
        pytest.param(28, 39, [3, 5], id="Human age over two years"),
        pytest.param(100, 100, [21, 17], id="Human age over two years"),
    ],
)
def test_of_different_age_variations(cat_age, dog_age, human_age):
    assert get_human_age(cat_age, dog_age) == human_age
