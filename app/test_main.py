import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (0, 0, [0, 0]),
        (14, 16, [0, 1]),
        (15, 15, [1, 1]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_should_return_correct_output(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
