from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0], id="0, 0"),
        pytest.param(14, 14, [0, 0], id="14, 14"),
        pytest.param(15, 15, [1, 1], id="15, 15"),
        pytest.param(23, 23, [1, 1], id="23, 23"),
        pytest.param(24, 24, [2, 2], id="24, 24"),
        pytest.param(27, 27, [2, 2], id="27, 27"),
        pytest.param(28, 28, [3, 2], id="28, 28"),
        pytest.param(100, 100, [21, 17], id="100, 100")
    ]
)
def test_age_by_value(cat_age: int, dog_age: int, expected: list) -> None:
    test = get_human_age(cat_age, dog_age)
    assert test == expected
    assert cat_age >= 0 and dog_age >= 0
    assert isinstance(test, list)
    assert all(isinstance(result, int) for result in test)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param(1, -2, id="negative dog age"),
        pytest.param(-3, 1, id="negative cat age "),
        pytest.param(-4, -2, id="both negative"),
    ]
)
def test_negative_value(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param(None, 123, id="Dog age is None"),
        pytest.param(33, [1 , 2], id="Cat age is list"),
        pytest.param({}, "nine", id="both incorrect type"),
    ]
)
def test_bad_value(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age_before, dog_age_before, cat_age_after, dog_age_after",
    [
        pytest.param(27, 28, 28, 29, id="every 5 year border"),
        pytest.param(23, 24, 24, 25, id="9 year border"),
        pytest.param(13, 14, 14, 15, id="first border"),
    ]
)
def test_borders(cat_age_before: int,
                 dog_age_before: int,
                 cat_age_after: int,
                 dog_age_after: int
                 ) -> None:
    before = get_human_age(cat_age_before, dog_age_before)
    after = get_human_age(cat_age_after, dog_age_after)
    assert before != after
