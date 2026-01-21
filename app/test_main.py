from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            14, 14, [0, 0],
            id="should add zeros with animal ages less than 15"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="add one when animal ages less than 24"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="add one more year when dog is 28, cat is 27"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="add one more year when dog is  28, cat is 27"
        ),
        pytest.param(
            120, 100, [26, 17],
            id="should return 26, 17 when dog 100 cat 120"
        ),
        pytest.param(
            1, 100, [0, 17],
            id="should return 0, 17 when dog 100 cat 1"
        ),
        pytest.param(
            -90, -70, [0, 0],
            id="should return zeros when ages are negative"
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "string", "string",
            TypeError,
            id="should raise value error when string is inputted"
        ),
        pytest.param(
            [0], [1, 7, "jj"],
            TypeError,
            id="should raise value error when list is inputted"
        ),
        pytest.param(
            {"Radiohead": "OK Computer", "10": 10}, {"one", "two"},
            TypeError,
            id="should raise value error when dict or tuple is inputted"
        ),
        pytest.param(
            {"one", "two"}, lambda a: a + 10,
            TypeError,
            id="should raise value error when set or function is inputted"
        )
    ]
)
def test_get_human_age_invalid_input(
        cat_age: int,
        dog_age: int,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
