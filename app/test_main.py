import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(-12, -13, [0, 0], id="out_of_range"),
        pytest.param(0, 0, [0, 0], id="out_of_range"),
        pytest.param(14, 14, [0, 0], id="edge_cases"),
        pytest.param(15, 15, [1, 1], id="edge_cases"),
        pytest.param(23, 23, [1, 1], id="edge_cases"),
        pytest.param(24, 24, [2, 2], id="edge_cases"),
        pytest.param(27, 27, [2, 2], id="edge_cases"),
        pytest.param(28, 28, [3, 2], id="edge_cases"),
        pytest.param(100, 100, [21, 17], id="out_of_range"),
    ]
)
def test_output(cat_age: int, dog_age: int, result: int) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("hello", "hi", id="str TypeError"),
        pytest.param([1], [2], id="list TypeError"),
    ]
)
def test_incorrect_types(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
