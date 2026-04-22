from typing import Any

import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, cat_expected_human_age, dog_expected_human_age",
    [
        (-1, -1, 0, 0),
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 27, 2, 2),
        (28, 28, 3, 2),
        (29, 29, 3, 3),
        (100, 100, 21, 17)
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        cat_expected_human_age: int,
        dog_expected_human_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [
        cat_expected_human_age,
        dog_expected_human_age
    ]


@pytest.mark.parametrize(
    "bad_input",
    [
        "twenty",
        5.5,
        None,
        [10, 20],
        {"five": 5},
        (3, 3)
    ]
)
def test_bad_input(bad_input: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(bad_input, bad_input)
