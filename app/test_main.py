from contextlib import nullcontext as not_raise

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result, description, expectation",
    [
        (14, 14, [0, 0], "Age less than 15 should return [0, 0]", not_raise()),
        (23, 23, [1, 1], "Age equals to 23 return [1, 1]", not_raise()),
        (24, 24, [2, 2], "When age 24 should return [2, 2]", not_raise()),
        (-1, -1, [0, 0], "Negative ages should return [0, 0]", not_raise()),
        (10.2, 10.2, [0, 0], "Not integer should return [0, 0]", not_raise()),
        (
            17,
            17,
            [1, 1],
            "When age equals to 15 and less than 24 should return [1, 1]",
            not_raise()
        ),
        (
            100,
            100,
            [21, 17],
            "When age 100 should return 21 for cat and 17 for dog",
            not_raise()
        ),
        ("cat", "dog", [0, 0], "Exception", pytest.raises(TypeError)),
        ("five", "five", [0, 0], "Exception", pytest.raises(TypeError)),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: int,
        description: str,
        expectation: pytest.fixture
) -> None:
    with expectation:
        assert get_human_age(cat_age, dog_age) == expected_result, description
