import pytest
from app.main import get_human_age



@pytest.mark.parametrize(
    "cat_age,dog_age,expected_ages",
    [
        pytest.param(0, 0, [0, 0],
                     id="should return [0, 0] if pets ages equal zeros"),
        pytest.param(14, 14, [0, 0],
                     id="should return [0, 0] if pets ages are less then 15"),
        pytest.param(-5, -5, [0, 0],
                     id="should return [0, 0] if pets have negatives ages"),
        pytest.param(15, 23, [1, 1],
                     id="should return [1, 1] if pets ages between 15 and 23"),
        pytest.param(24, 27, [2, 2],
                     id="should return [2, 2] if pets ages between 24 and 27"),
        pytest.param(28, 28, [3, 2],
                     id="should return [3, 2] if pets ages are equal 28"),
        pytest.param(100, 100, [21, 17],
                     id="should return [21, 17] if pets ages are equal 100")
    ]
)
def test_get_human_age(cat_age, dog_age, expected_ages):
    assert get_human_age(cat_age, dog_age) == expected_ages
