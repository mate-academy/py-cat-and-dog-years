import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(0,
                     0,
                     [0, 0],
                     id="return 0 when dog and cat age is 0"),
        pytest.param(14,
                     14,
                     [0, 0],
                     id="14 cats and dogs years = 0 human years"),
        pytest.param(15,
                     15,
                     [1, 1],
                     id="15 dog and cat years = 1 human"),
        pytest.param(24,
                     24,
                     [2, 2],
                     id="24 dog and cat years = 2 human"),
        pytest.param(28,
                     28,
                     [3, 2],
                     id="28 dog years = 3 human and 28 cat years = 2 human"),
        pytest.param(100,
                     100,
                     [21, 17],
                     id=("100 dog years =21 human, 100 cat years =17 human")),
    ]
)
def test_can_sum(cat_age: int, dog_age: int, human_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param("15",
                     "20",
                     id="must be an int (not a string)"),
        pytest.param([],
                     [],
                     id="must be an int (not a list)"),
        pytest.param({},
                     {},
                     id="must be an int (not a dict)"),
        pytest.param(15,
                     {},
                     id="Correct! must be an int (not a dict)"),
        pytest.param("15",
                     {},
                     id="Correct! must be an int (not a dict and str)"),
        pytest.param("15",
                     [],
                     id="Correct! must be an int (not a list and str)"),
        pytest.param([],
                     {},
                     id="Correct! must be an int (not a dict and list)"),
    ]
)
def test_can_sum_invalid_inputs(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
