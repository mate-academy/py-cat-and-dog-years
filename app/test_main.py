from typing import List
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_common_cases(cat_age: int, dog_age: int,
                                    expected: List[int]) -> None:
    """Test normal valid inputs."""
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-100, -100),
    ]
)
def test_negative_ages_return_zero(cat_age: int, dog_age: int) -> None:
    """Negative ages are treated as less than first_year → returns 0."""
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 10),
        (10, "5"),
        ("abc", "xyz"),
        (10.5, 20),
        (10, 20.8),
        ([], {}),
        (None, None),
    ]
)
def test_invalid_types_raise_exception(cat_age: int, dog_age: int) -> None:
    """Incorrect types MUST raise TypeError."""
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
