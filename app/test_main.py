import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0],
                     id="Cat and dog are 0 years old"),
        pytest.param(14, 14, [0, 0],
                     id="Cat and dog are less than 15 years old"),
        pytest.param(15, 15, [1, 1],
                     id="Cat and dog are exactly 15 years old"),
        pytest.param(23, 23, [1, 1],
                     id="Cat and dog are 23 years old"),
        pytest.param(24, 24, [2, 2],
                     id="Cat and dog are exactly 24 years old"),
        pytest.param(27, 27, [2, 2],
                     id="Cat and dog are 27 years old"),
        pytest.param(28, 28, [3, 2],
                     id="Cat and dog are 28 years old"),
        pytest.param(100, 100, [21, 17],
                     id="Cat and dog are 100 years old"),
        pytest.param(-5, -5, [0, 0],
                     id="Negative age values (cat and dog)"),
        pytest.param(500, 500, [121, 97],
                     id="Extremely large age values (cat and dog)"),
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected: list[int]) -> None:
    """Test get_human_age function with various parameters."""
    assert get_human_age(cat_age, dog_age) == expected
