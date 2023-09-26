import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [

    (0, 0, [0, 0]),
    (14, 0, [0, 0]),
    (15, 0, [1, 0]),
    (23, 0, [1, 0]),
    (24, 0, [2, 0]),
    (27, 0, [2, 0]),
    (28, 0, [3, 0]),
    (100, 0, [21, 0]),
    (0, 14, [0, 0]),
    (0, 15, [0, 1]),
    (0, 23, [0, 1]),
    (0, 24, [0, 2]),
    (0, 27, [0, 2]),
    (0, 28, [0, 2]),
    (0, 100, [0, 17]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    ("14", 14, TypeError),
    (14, "14", TypeError),
    ("value", 1, TypeError),
    (1, "value", TypeError),
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: tuple
) -> None:
    if isinstance(expected_result, list):
        assert get_human_age(cat_age, dog_age) == expected_result
    elif expected_result == TypeError:
        with pytest.raises(expected_result):
            get_human_age(cat_age, dog_age)
