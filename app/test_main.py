import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(3, 6, [0, 0], id="less than 1 year"),
        pytest.param(15, 15, [1, 1], id="1 year"),
        pytest.param(27, 18, [2, 2], id="2 years"),
        pytest.param(29, 29, [3, 3], id="3 years"),
        pytest.param(50, 50, [8, 7], id="add different extra years"),
        pytest.param(1000, 1000, [246, 197], id="big values"),
        pytest.param(-1, -59, [0, 0], id="numbers less than zero")
    ]
)
def test_get_human_age_diff_values(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        pytest.param("3", [2, 5], TypeError, id="age should be integer"),
        pytest.param(1, {2, 5}, TypeError, id="age should be integer"),
        pytest.param({"3": "20"}, True, TypeError, id="age should be integer"),
        pytest.param([2, 5], (5, 9), TypeError, id="age should be integer")
    ]
)
def test_get_human_age_wrong_types(
        cat_age: int,
        dog_age: int,
        error: TypeError
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
