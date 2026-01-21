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
    assert isinstance(test, list)
    assert all(isinstance(result, int) for result in test)


@pytest.mark.parametrize(
    "cat_age",
    [
        pytest.param(-3, id="negative cat age"),
        pytest.param(-4, id="negative cat age"),
    ]
)
def test_cat_negative_value(cat_age: int) -> None:
    result = get_human_age(cat_age, 1)
    assert result[0] == 0


@pytest.mark.parametrize(
    "dog_age",
    [
        pytest.param(-3, id="negative cat age"),
        pytest.param(-4, id="negative cat age"),
    ]
)
def test_dog_negative_value(dog_age: int) -> None:
    result = get_human_age(1, dog_age)
    assert result[1] == 0


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param(None, None, id="Both is none"),
        pytest.param("S", "w", id="Both is string"),
        pytest.param([], {"w": 123}, id="Random type"),
    ]
)
def test_bad_value(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age_before, cat_age_after, expected_result",
    [
        pytest.param(27, 28, True, id="cat 5 year boarder"),
        pytest.param(27, 27, False, id="cat 5 year boarder"),
        pytest.param(23, 24, True, id="cat 9 year boarder"),
        pytest.param(22, 23, False, id="cat 9 year boarder"),
        pytest.param(14, 15, True, id="cat 15 year boarder"),
        pytest.param(14, 13, False, id="cat 15 year boarder")
    ]
)
def test_cat_age_borders(cat_age_before: int,
                         cat_age_after: int,
                         expected_result: bool
                         ) -> None:
    before = get_human_age(cat_age_before, 1)
    after = get_human_age(cat_age_after, 1)
    if expected_result:
        assert before[0] != after[0]
    else:
        assert before[0] == after[0]


@pytest.mark.parametrize(
    "dog_age_before, dog_age_after, expected_result",
    [
        pytest.param(28, 29, True, id="dog 5 year boarder"),
        pytest.param(27, 28, False, id="dog 5 year boarder"),
        pytest.param(23, 24, True, id="dog 9 year boarder"),
        pytest.param(22, 23, False, id="dog 9 year boarder"),
        pytest.param(14, 15, True, id="dog 15 year boarder"),
        pytest.param(14, 13, False, id="dog 15 year boarder")
    ]
)
def test_dog_age_borders(dog_age_before: int,
                         dog_age_after: int,
                         expected_result: bool
                         ) -> None:
    before = get_human_age(1, dog_age_before)
    after = get_human_age(1, dog_age_after)
    if expected_result:
        assert before[1] != after[1]
    else:
        assert before[1] == after[1]
