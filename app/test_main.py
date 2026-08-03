from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0], id="0 pet years"),
        pytest.param(-5, -10, [0, 0],
                     id="Negative pet years should return zeros"),
        pytest.param(14, 14, [0, 0], id="Less then 15 pet years"),
        pytest.param(15, 15, [1, 1], id="Pet 15 years equal 1 human"),
        pytest.param(23, 23, [1, 1], id="Pet 23 years equal 1 human"),
        pytest.param(27, 27, [2, 2], id="Pet 27 years equal 2 human"),
        pytest.param(28, 28, [3, 2],
                     id="Cat 28 years equal 3 human "
                        "and dog 28 years equal 2 human"),
        pytest.param(28, 29, [3, 3],
                     id="Cat 28 years equal 3 human and dog "
                        "28 years equal 3 human"),
        pytest.param(100, 100, [21, 17], id="100 pet years"),
        pytest.param(1000, 1000, [246, 197], id="Really large numbers "
                                                "(1000 pet years)"),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "invalid_cat_age, invalid_dog_age",
    [
        pytest.param(15.5, 15, id="Float cat age"),
        pytest.param(15, 15.0, id="Float dog age"),
        pytest.param("15", 15, id="String cat age"),
        pytest.param(True, 15, id="Bool cat age"),
    ]
)
def test_get_human_age_raises_type_error_on_invalid_types(
        invalid_cat_age: Any,
        invalid_dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(invalid_cat_age, invalid_dog_age)
