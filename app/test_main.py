from typing import Any

import pytest

from app.main import get_human_age


# -------------Test valid boundary conditions--------------

@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="both zero"),
        pytest.param(14, 14, [0, 0], id="just below first threshold"),
        pytest.param(23, 23, [1, 1], id="just below second threshold"),
        pytest.param(-100, -100, [0, 0], id="negative values"),
        pytest.param(10000, 10000, [2496, 1997], id="very large values"),
        pytest.param(15, 0, [1, 0], id="cat first human year"),
        pytest.param(24, 0, [2, 0], id="cat second human year"),
        pytest.param(40, 0, [6, 0], id="cat extra years"),
        pytest.param(0, 15, [0, 1], id="dog first human year"),
        pytest.param(0, 24, [0, 2], id="dog second human year"),
        pytest.param(0, 49, [0, 7], id="dog extra years"),
    ]
)
def test_get_human_age_with_valid_values(
    cat_age: int,
    dog_age: int,
    result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


# -------------Test invalid input types--------------

@pytest.mark.parametrize(
    "cat_age,dog_age,exception",
    [
        pytest.param("0", "0", TypeError, id="string inputs"),
        pytest.param(14, None, TypeError, id="dog is NoneType"),
        pytest.param(None, 16, TypeError, id="cat is NoneType"),
    ]
)
def test_get_human_age_with_wrong_values_types(
    cat_age: Any,
    dog_age: Any,
    exception: Exception
) -> None:
    with pytest.raises(exception):
        get_human_age(cat_age, dog_age)
