from typing import Any
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_list",
    [
        pytest.param(0, 0, [0, 0], id="should return list with 0"),
        pytest.param(14, 14, [0, 0], id="before 15"),
        pytest.param(15, 15, [1, 1], id="should return list with 1"),
        pytest.param(23, 23, [1, 1], id="before 23"),
        pytest.param(24, 24, [2, 2], id="should return list with 2"),
        pytest.param(27, 27, [2, 2], id="after 24"),
        pytest.param(28, 28, [3, 2], id="at 28"),
        pytest.param(29, 29, [3, 3], id="after 28"),
        pytest.param(100, 100, [21, 17], id="big numbers"),
        pytest.param(1.5, 0, [0, 0], id="cat_float age"),
        pytest.param(-1, 2, [0, 0], id="negative_age"),
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_list: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_list

@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(1, "1", TypeError, id="dog_str age"),
    ]
)
def test_get_human_age_error(cat_age: Any, dog_age: Any, expected_error) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)