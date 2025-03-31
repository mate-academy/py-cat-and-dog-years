from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(-20, -20, [0, 0], id="check -20 years"),
        pytest.param(0, 0, [0, 0], id="check 0 years"),
        pytest.param(14, 14, [0, 0], id="check 14 years"),
        pytest.param(15, 15, [1, 1], id="check 15 years"),
        pytest.param(23, 23, [1, 1], id="check 23 years"),
        pytest.param(24, 24, [2, 2], id="check 24 years"),
        pytest.param(27, 27, [2, 2], id="check 27 years"),
        pytest.param(28, 28, [3, 2], id="check 28 years"),
        pytest.param(100, 100, [21, 17], id="check 100 years"),

    ]
)
def test_cat_dog_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:

    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param("0", 0, [0, 0], id="check str type"),
        pytest.param(14, [1], [0, 0], id="check list type"),
        pytest.param({"123": 123}, "1", [0, 0], id="check dick and str type"),
    ]
)
def test_incorrect_data(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:

    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
