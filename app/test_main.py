import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (10, 10, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (20, 20, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (30, 30, [3, 3]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int,
                       expected_result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result, (
        f"Expected result for cat_age={cat_age} and dog_age={dog_age} is "
        f"{expected_result}"
    )
