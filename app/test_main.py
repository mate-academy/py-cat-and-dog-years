import pytest

from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(0, 0, [0, 0], id="all zero's"),
        pytest.param(14, 14, [0, 0], id="cat and dog age < 14"),
        pytest.param(23, 24, [1, 2], id="cat and dog are < 24 y.o."),
        pytest.param(28, 28, [3, 2], id="Cat age >= 28, dog age < 29"),
        pytest.param(100, 100, [21, 17], id="Test large numbers")
    ]
)
def test_get_human_age(cat_age: Any,
                       dog_age: Any,
                       expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(5, "10", TypeError, id="Wrong type"),
        pytest.param({10}, 5, TypeError, id="Wrong type")
    ]
)
def test_for_errors(cat_age: Any,
                    dog_age: Any,
                    expected_error: Any) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
