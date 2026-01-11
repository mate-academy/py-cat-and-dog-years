from typing import Any

from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(28, 28, [3, 2], id="default test 28"),
        pytest.param(27, 27, [2, 2], id="default test 27"),
        pytest.param(23, 23, [1, 1], id="default test 23"),
        pytest.param(14, 14, [0, 0], id="default test 14"),
        pytest.param(15, 15, [1, 1], id="default test 15"),
        pytest.param(24, 24, [2, 2], id="default test 15"),
    ]
)
def test_works_correctly(
        cat_age: int,
        dog_age: int,
        human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(-1, 10, ValueError, id="negative cat age"),
        pytest.param(10, -1, ValueError, id="negative dog age"),
        pytest.param("5", 10, TypeError, id="string cat age"),
        pytest.param(10, 5.5, TypeError, id="float dog age"),
        pytest.param(10, 10000000, ValueError, id="too large dog age"),

    ]
)
def test_raises_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Any) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
