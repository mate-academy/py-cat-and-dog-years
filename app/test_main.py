import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="0 years"),
        pytest.param(14, 14, [0, 0], id="14 years"),
        pytest.param(15, 15, [1, 1], id="15 years"),
        pytest.param(23, 23, [1, 1], id="23 years"),
        pytest.param(24, 24, [2, 2], id="24 years"),
        pytest.param(27, 27, [2, 2], id="27 years"),
        pytest.param(28, 28, [3, 2], id="28 years"),
        pytest.param(100, 100, [21, 17], id="100 years"),
        pytest.param(0, 0, [0, 0], id="Zero values"),
        pytest.param(-1, -1, [0, 0], id="Negative values"),
        pytest.param(1000, 10000, [246, 1997], id="Large values")
    ]
)
def test_return_value(
        cat_age: int, dog_age: int, result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("string", 0, id="string"),
        pytest.param([1], 0, id="list"),
        pytest.param({1}, 0, id="dict")
    ]
)
def test_type_error_exception(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
