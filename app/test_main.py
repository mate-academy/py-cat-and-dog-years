from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        pytest.param(0, 0, [0, 0],
                     id="Check if age is 0"),
        pytest.param(14, 14, [0, 0],
                     id="Check if age is 14"),
        pytest.param(15, 15, [1, 1],
                     id="Check if age is 15"),
        pytest.param(23, 23, [1, 1],
                     id="Check if age is 23"),
        pytest.param(24, 24, [2, 2],
                     id="Check if age is 24"),
        pytest.param(27, 27, [2, 2],
                     id="Check if age is 27"),
        pytest.param(28, 28, [3, 2],
                     id="Check if age is 28"),
        pytest.param(100, 100, [21, 17],
                     id="Check if age is 100")
    ]
)
def test_get_human_age_from_range_ages(
        cat_age: int,
        dog_age: int,
        expected_human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age
