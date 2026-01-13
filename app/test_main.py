import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (15, 15, [15, 15]),
        (24, 24, [16, 16]),
        (30, 35, [17, 18]),
    ]
)
def test_human_age_conversion(cat_age: int,
                              dog_age: int,
                              expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected
