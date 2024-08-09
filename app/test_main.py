import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result, description",
    [
        (14, 14, [0, 0], "Age less than 15 should return [0, 0]"),
        (24, 24, [2, 2], "When age 24 should return [2, 2]"),
        (-1, -1, [0, 0], "Negative ages should return [0, 0]"),
        (10.2, 10.2, [0, 0], "Not integer should return [0, 0]"),
        (
            17,
            17,
            [1, 1],
            "When age equals to 15 and less than 24 should return [1, 1]"
        ),
        (
            100,
            100,
            [21, 17],
            "When age 100 should return 21 for cat and 17 for dog"
        ),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: int,
        description: str
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result, description
