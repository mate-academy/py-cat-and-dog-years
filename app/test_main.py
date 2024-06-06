import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [   
        pytest.param(14, 15, [0, 1], id="Cat in the first range < 15, Dog in the second range >= 15"),
        pytest.param(23, 24, [1, 2], id="Cat in the second range < 24, Dog in second range >= 24"),
        pytest.param(28, 28, [3, 2], id="After ranges step for Cat + 4, for Dog + 5"),
    ]
)
def test_valid_inputs(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
    
@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="with 2 zeros"),
        pytest.param(-1, -1, [0, 0], id="with negative numbers"),
        pytest.param(100, 100, [21, 17], id="function not correct working with large numbers")
    ]
)
def test_specific_inputs(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
    
@pytest.mark.parametrize(
    "cat_age,dog_age,error_type",
    [
        pytest.param("1", "2", TypeError)
    ]
)
def test_error_case(cat_age: int, dog_age: int, error_type: Exception) -> None:
    with pytest.raises(error_type):
        get_human_age(cat_age, dog_age)
