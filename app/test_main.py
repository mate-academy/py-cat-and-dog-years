import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(-5, -5, [0, 0], id="when animals age are negative"),
        pytest.param(0, 0, [0, 0], id="when animals age are 0"),
        pytest.param(14, 14, [0, 0], id="when animals age are 14"),
        pytest.param(15, 15, [1, 1], id="when animals age are 15"),
        pytest.param(23, 23, [1, 1], id="when animals age are 23"),
        pytest.param(24, 24, [2, 2], id="when animals age are 24"),
        pytest.param(27, 27, [2, 2], id="when animals age are 27"),
        pytest.param(28, 28, [3, 2], id="when animals age are 28"),
        pytest.param(29, 29, [3, 3], id="when animals age are 29"),
        pytest.param(500, 500, [121, 97], id="when animals age are very big")
    ]
)
def test_func_should_return_the_right_results(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("1", "1", id="when data is string"),
        pytest.param([1], [1], id="when data is list"),
        pytest.param({1}, {1}, id="when data is set"),
    ]
)
def test_func_raise_type_error_when_receives_incorrect_data(
        cat_age: int,
        dog_age: int,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
