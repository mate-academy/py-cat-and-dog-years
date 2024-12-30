import pytest
from app.main import get_human_age
from typing import Any


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        # (-30, 16, [0, 1]),
        # (10, -10, [0, 0]),
        (1.6, 35.5, [0, 4]),
        (500, 1000000, [121, 199997])
    ]
)
def test_convert_to_human_correctly(
        cat_age: int,
        dog_age: int,
        human_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            "12",
            22,
            TypeError,
            id="should raise error "
               "if the function receives an incorrect type of data"
        ),
        pytest.param(
            35,
            "55",
            TypeError,
            id="should raise error "
               "if the function receives an incorrect type of data"
        )
    ]
)
def test_raising_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
