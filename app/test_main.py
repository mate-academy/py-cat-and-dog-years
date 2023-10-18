from typing import Any
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_age",
    [
        pytest.param(0, 0, [0, 0], id="Age of human = 0"),
        pytest.param(15, 15, [1, 1], id="Age of human = 1"),
        pytest.param(28, 28, [3, 2], id="Age of human = 3, 2 years"),
        pytest.param(100, 100, [21, 17], id="Age of human = 21 and 17y.o"),
        pytest.param(-1, 15, [0, 1], id="Age of human = 1"),
        pytest.param(28, 39, [3, 5], id="Age of human = 3 and 5y.o"),
        pytest.param("cat age", 20, None, id="Cat age isn`t int!"),
        pytest.param(15, "dog age", None, id="Dog age isn`t int!"),
        pytest.param("cat age", "dog age", None, id="Both ages are not int!"),
        pytest.param({"cat": 10}, {"dog": 12}, None, id="Dictionary input"),
        pytest.param((5, 10), (3, 8), None, id="Tuple input"),
        pytest.param({1, 2, 3}, {4, 5, 6}, None, id="Set input"),
        pytest.param([8, 9], [10, 11, 12], None, id="List input"),
    ]
)
def test_get_human_age(
        cat_age: Any,
        dog_age: Any,
        expected_age: list | None
) -> None:
    if expected_age is not None:
        assert get_human_age(cat_age, dog_age) == expected_age
    else:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
