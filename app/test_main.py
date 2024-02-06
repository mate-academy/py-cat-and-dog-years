import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (15, 15, [1, 1]),
    (14, 14, [0, 0]),
    (27, 28, [2, 2]),
    (24, 24, [2, 2]),
    (28, 29, [3, 3]),
    (23, 23, [1, 1])
]
)
def test_to_check_correct_conversion(cat_age: int, dog_age: int,
                                     expected: list) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected
