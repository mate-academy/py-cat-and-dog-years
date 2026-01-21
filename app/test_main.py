import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 28, [2, 2]),
    (28, 29, [3, 3]),
])
def test_age_conversion(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_wrong_types() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat_age", 14)
    with pytest.raises(TypeError):
        get_human_age(14, "dog_age")
    with pytest.raises(TypeError):
        get_human_age("cat_age", "dog_age")
