import pytest
from typing import Any


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        ("12", 0, ValueError),
        (17, "ktc", ValueError),
        ("dkf", "zkd", ValueError),
        (-1, 23, ValueError),
        (24, 200, ValueError),
        (-15, 202, ValueError),
    ]
)
def test_human_age_has_proper_inputs(cat_age: Any,
                                     dog_age: Any,
                                     expected_exception: Any) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_human_age_conversion(cat_age: Any,
                              dog_age: Any,
                              expected_human_age: Any) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age
