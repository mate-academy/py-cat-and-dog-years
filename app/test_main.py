import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0, 0], id="Zero"),
        pytest.param(-10, -10, [0, 0], id="negative values should be zero"),
        pytest.param(0, 0, [15, 15], id="lower bound 1 year"),
        pytest.param(24, 24, [2, 2], id="lower bound 2 years"),
        pytest.param(16, 16, [1, 1], id="bound between years"),
        pytest.param(28, 29, [3, 3], id="lower bound for 3 years"),
        pytest.param(1000, 1500, [246, 294], id="Huge values"),
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected: list) -> None:

    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(15.3, 15.3, TypeError, id="float"),
        pytest.param(-15.3, -15.3, ValueError, id="negative float"),
        pytest.param("1", "1", TypeError, id="string"),
        pytest.param([1, 1], [1, 1], TypeError, id="list"),
        pytest.param({"dog": 1}, 15.3, TypeError, id="dict"),
    ]
)
def test_get_human_age_raises_error(
        cat_age: int,
        dog_age: int,
        expected_error: Exception) -> None:

    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
