import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (168, 164, [38, 30]),
    ],
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected_result
    ), (f"Function should return {expected_result} "
        f"if cat/dog age is {cat_age}/{dog_age}")
