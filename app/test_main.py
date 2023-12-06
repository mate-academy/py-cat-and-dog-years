import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(28, 28, [3, 2], id="normal values"),
        pytest.param(100, 100, [21, 17], id="large values"),
        pytest.param(-1, -1, [0, 0], id="negative values"),
        pytest.param(0, 0, [0, 0], id="values is 0"),
        pytest.param(100.0, 100.0, [21.0, 17.0], id="values is float")
    ]
)
def test_different_values(
        cat_age: int | float,
        dog_age: int | float,
        expected_result: int | float
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("28", "28", id="values is str"),
        pytest.param([100], [100], id="values is list"),
    ]
)
def test_incorrect_type(
        cat_age: int | float,
        dog_age: int | float
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
